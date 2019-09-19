import tkinter as tk
from tkinter import messagebox as tkMessageBox


class PopupViewUndergrad(tk.Frame):
    """ Popup Window """

    def __init__(self, parent, close_popup_callback, student, update_button):
        """ Initialize the nav bar """
        tk.Frame.__init__(self, parent)
        self._parent = parent
        self.grid(rowspan=2, columnspan=3, padx=20, pady=20)

        self._close_popup_callback = close_popup_callback
        self._student = student
        self._update_button = update_button
        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for the popup window """

        self._label = tk.Label(self, text = "Update Undergraduate Student", justify = tk.LEFT).grid(row=0, columnspan=3 )
        self._first_name = tk.Label(self, text="First Name").grid(row = 1, column = 0)
        self._last_name = tk.Label(self, text="Last Name").grid(row =2,column = 0)
        self._program = tk.Label(self, text="Program").grid(row =3, column = 0)
        self._classification = tk.Label(self, text="Classification").grid(row =4, column = 0)
        self._enroll_status = tk.Label(self, text="Enroll status").grid(row =5, column = 0)
        self._enroll_date = tk.Label(self, text="Enroll date").grid(row =6, column = 0)
        #self._type = tk.Label(self, text="Type").grid(row =7, column = 0)
        self._minor = tk.Label(self, text="Minor").grid(row =8, column = 0)
        self._min_credit = tk.Label(self, text="Miniumn credit").grid(row =9, column = 0)

        self.e_first_name = tk.Entry(self)
        self.e_first_name.grid(row=1, column=1)
        self.e_last_name = tk.Entry(self)
        self.e_last_name.grid(row=2, column=1)
        self.e_program = tk.Entry(self)
        self.e_program.grid(row=3, column=1)
        self.e_classification = tk.Entry(self)
        self.e_classification.grid(row=4, column=1)
        self.e_enroll_status = tk.Entry(self)
        self.e_enroll_status.grid(row=5, column=1)
        self.e_enroll_date = tk.Entry(self)
        self.e_enroll_date.grid(row=6, column=1)
        # self.e_type = tk.Entry(self)
        # self.e_type.grid(row=7, column=1)
        self.e_minor = tk.Entry(self)
        self.e_minor.grid(row=8, column=1)
        self.e_min_credit = tk.Entry(self)
        self.e_min_credit.grid(row=9, column=1)


        self._button1 = tk.Button(self,
                  text="Update",
                  command=self._update_button).grid(row=10, column=0)

        self._button2 =  tk.Button(self,
                   text="Close",
                   command=self._close_popup_callback).grid(row=10, column=1)

    def set_data(self):
        self.e_first_name.insert(0, self._student['first_name'])
        self.e_last_name.insert(0, self._student['last_name'])
        self.e_program.insert(0, self._student['program'])
        self.e_classification.insert(0,self._student['classification'])
        self.e_enroll_status.insert(0, self._student['enroll_status'])
        self.e_enroll_date.insert(0, self._student['enroll_date'])
        # self.e_type.insert(0, self._student['type'])
        self.e_minor.insert(0, self._student['minor'])
        self.e_min_credit.insert(0, self._student['minimum_credit'])

    def get_data(self):
        min_credit = self.e_min_credit.get()
        if min_credit.isdigit():
            min_credit = int(min_credit)


        data = {"first_name": self.e_first_name.get(), "last_name": self.e_last_name.get(),
                     "program": self.e_program.get(), "classification": self.e_classification.get(),
                     "enroll_status": self.e_enroll_status.get(), "enroll_date":self.e_enroll_date.get(),
                     "type":"Undergraduate", "minor":self.e_minor.get(), "minimum_credit":min_credit}
        return data

    def update(self):
        """ update undergrad students file """
        if tkMessageBox.askyesno('Verify', 'Really update?'):
            return True
        return False

    def message_box(self, status_code):
        if status_code == 200:
            tkMessageBox.showinfo("Success", "Student record is updated!")
        else:
            tkMessageBox.showerror("Error", "Student is invalid or missing data.")
