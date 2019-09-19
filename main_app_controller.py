import tkinter as tk
from top_navbar_view import TopNavbarView
from display_undergraduate import DisplayUndergraduate
from display_graduate import DisplayGraduate
from add_undergrad_popup import AddUndergradPopup
from add_grad_popup import AddGradPopup
from popup_view_update_undergrad import PopupViewUndergrad
from popup_view_update_grad import PopupViewGraduate
from bottom_navbar_view import BottomNavbarView
from view_grad_details import ViewGradDetails
from view_undergrad_details import ViewUndergradDetails
from tkinter import messagebox as tkMessageBox
import requests


class MainAppController(tk.Frame):
    """ Main Application for GUI """

    def __init__(self, parent):
        """ Initialize Main Application """

        tk.Frame.__init__(self, parent)
        self._top_navbar = TopNavbarView(self, self._page_callback )
        self._display_undergrad= DisplayUndergraduate(self, self._undergrad_submit_callback, self._add_undergrad_popup_callback,
                                                      self._update_undergrad_popup_callback, self._delete_undergrad_callback,
                                                      self._view_undergrad_callback)
        self._display_grad= DisplayGraduate(self, self._grad_submit_callback, self._add_grad_popup_callback,
                                            self._update_grad_popup_callback, self._delete_grad_callback,
                                            self._view_grad_callback)
        self._bottom_navbar = BottomNavbarView(self, self._quit_callback)



        self._top_navbar.grid(row=0, columnspan=10, pady=10, padx= 10)
        self._display_undergrad.grid(row=1, columnspan=10)
        self._curr_page = TopNavbarView.UNDERGRADUATE
        self._bottom_navbar.grid(row=6, column=3, pady=10)

        self._students = []



    def _page_callback(self):
        """ Handle Switching Between Pages """

        curr_page = self._top_navbar.curr_page.get()
        if (self._curr_page != curr_page and self._curr_page == TopNavbarView.UNDERGRADUATE):
            self._display_undergrad.grid_forget()
            self._display_grad.grid(row=1, column=4)
            self._curr_page = TopNavbarView.GRADUATE
            self._grad_submit_callback()
        elif (self._curr_page != curr_page and self._curr_page == TopNavbarView.GRADUATE):
            self._display_grad.grid_forget()
            self._display_undergrad.grid(row=1, column=4)
            self._curr_page = TopNavbarView.UNDERGRADUATE
            self._undergrad_submit_callback()

    def _add_grad_popup_callback(self):
        """ Add Graduate students popup """

        self._popup_win = tk.Toplevel()
        self._popup = AddGradPopup(self._popup_win, self._close_popup_callback, self._add_button)

    def _add_undergrad_popup_callback(self):
        """ Add Undergraduate students popup """
        self._popup_win = tk.Toplevel()
        self._popup = AddUndergradPopup(self._popup_win, self._close_popup_callback, self._add_button)


    def _add_button(self):
        """ Add Button students popup """

        data = self._popup.get_data()
        headers= {"content-type":"application/json"}
        response = requests.post("http://127.0.0.1:5000/studentmanager/students",
                                 json = data, headers = headers)

        if response.status_code == 200:
            self._grad_submit_callback()
            self._undergrad_submit_callback()
            self._popup.message_box(200)
            self._popup_win.destroy()

        else:
            self._popup.message_box(400)


    def _update_button(self):
        """ Update Button students popup """
        if self._popup.update():
            data = self._popup.get_data()
            id = self._student['id']
            headers= {"content-type":"application/json"}
            response = requests.put("http://127.0.0.1:5000/studentmanager/students/" + str(id),
                                     json = data, headers = headers)

            if response.status_code == 200:
                self._popup.message_box(200)
                self._popup_win.destroy()
            else:
                self._popup.message_box(400)

        self._undergrad_submit_callback()

    def _update_grad_popup_callback(self):
        """ Update Graduate students popup """
        id = self.get_id("graduate")
        response = requests.get("http://127.0.0.1:5000/studentmanager/students/" + str(id))
        self._student = response.json()

        self._popup_win = tk.Toplevel()
        self._popup = PopupViewGraduate(self._popup_win, self._close_popup_callback, self._student, self._update_button)
        self._popup.set_data()
        self._grad_submit_callback()



    def _update_undergrad_popup_callback(self):
        """ Update Undergraduate students popup """
        id = self.get_id("undergraduate")
        response = requests.get("http://127.0.0.1:5000/studentmanager/students/" + str(id))
        self._student = response.json()

        self._popup_win = tk.Toplevel()
        self._popup = PopupViewUndergrad(self._popup_win, self._close_popup_callback, self._student, self._update_button)
        self._popup.set_data()

        self._grad_submit_callback()
        self._undergrad_submit_callback()


    def get_id(self,display_view):
        """ Get id of the students """

        if display_view == "graduate":
            index = self._display_grad.get_index()
        elif display_view == "undergraduate":
            index = self._display_undergrad.get_index()

        id = self._students[index]['id']

        return id


    def _close_popup_callback(self):
        """ close popup window """
        self._popup_win.destroy()

    def _undergrad_submit_callback(self):
        """ Undergrad submit method """
        response = requests.get('http://127.0.0.1:5000/studentmanager/students/all/Undergraduate')

        if response.status_code == 200:
            self._students = response.json()
            self._display_undergrad.get_form_data(self._students)
            # print(self._students[0])

    def _grad_submit_callback(self):
        """ graduates student submit method """

        response = requests.get('http://127.0.0.1:5000/studentmanager/students/all/Graduate')
        if response.status_code == 200:
            self._students = response.json()
            self._display_grad.get_form_data(self._students)



    def _delete_undergrad_callback(self):
        """ Delete Undergrad students """

        id = self.get_id('undergraduate')

        if self._display_undergrad.delete():
            print(id)
            response = requests.delete('http://127.0.0.1:5000/studentmanager/students/' + str(id))
            if response.status_code == 200:
                tkMessageBox.showinfo("Success", "Student record is deleted!")
            else:
                tkMessageBox.showerror("Error")

        self._undergrad_submit_callback()



    def _delete_grad_callback(self):
        """ Delete graduate students """
        id = self.get_id('graduate')

        if self._display_grad.delete():
            response = requests.delete('http://127.0.0.1:5000/studentmanager/students/' + str(id))
            if response.status_code == 200:
                tkMessageBox.showinfo("Success", "Student record is deleted!")
            else:
                tkMessageBox.showerror("Error")

        self._grad_submit_callback()



    def _view_grad_callback(self):
        """view details for grad student"""
        id = self.get_id("graduate")
        response = requests.get("http://127.0.0.1:5000/studentmanager/students/" + str(id))
        self._student = response.json()

        self._popup_win = tk.Toplevel()
        self._popup = ViewGradDetails(self._popup_win, self._close_popup_callback, self._student)

    def _view_undergrad_callback(self):
        """view details for undergrad student"""
        id = self.get_id("undergraduate")
        response = requests.get("http://127.0.0.1:5000/studentmanager/students/" + str(id))
        self._student = response.json()

        self._popup_win = tk.Toplevel()
        self._popup = ViewUndergradDetails(self._popup_win, self._close_popup_callback, self._student)


    def _quit_callback(self):
        ''' quit GUI '''
        self.quit()




if __name__ == "__main__":
    root = tk.Tk()
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()
