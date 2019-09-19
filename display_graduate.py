import tkinter as tk
from tkinter import messagebox as tkMessageBox


class DisplayGraduate(tk.Frame):
    """ Display page """

    def __init__(self, parent, submit_callback, add_popup_callback, update_popup_callback, delete_popup_callback, view_popup_callback):
        """ Initialize Page 1 """
        tk.Frame.__init__(self, parent, width=800, height=800)
        self._parent = parent

        self._submit_callback = submit_callback
        self._add_popup_callback = add_popup_callback
        self._update_popup_callback = update_popup_callback
        self._delete_popup_callback = delete_popup_callback
        self._view_popup_callback = view_popup_callback


        self._students=[]


        self._create_widgets()
    def _create_widgets(self):
        """ Creates the widgets for Page 1 """
        self._title = tk.Label(self, text='Graduate')
        self._title.grid(row=1, column=2)

        self._scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self._listbox = tk.Listbox(self, yscrollcommand=self._scrollbar.set)
        self._listbox.grid(rowspan=5, columnspan=5)
        self._scrollbar.grid(row=2, column=3, sticky=tk.N + tk.S + tk.W + tk.E)

        self._button = tk.Button(self,
                                 text="Refresh",
                                 command=self._submit_callback)
        self._button.grid(row=7, column=2, padx=20)

        tk.Button(self,
                  text="Add",
                  command=self._add_popup_callback).grid(row=2, column=6)
        tk.Button(self,
                  text="Update",
                  command=self._update_popup_callback).grid(row=3, column=6, pady=5)
        tk.Button(self,
                  text="Delete",
                  command=self._delete_popup_callback).grid(row=4, column=6)
        tk.Button(self,
                  text="View Details",
                  command=self._view_popup_callback).grid(row=5, column=6)

    def get_form_data(self, data):
        """ display data on the listbox """
        self._listbox.delete(0, tk.END)
        for student in data:
            self._listbox.insert(tk.END, student['first_name'] +' '+ student['last_name'])
        # return { "name": self._entry_name.get() }

    def delete(self):
        """ delete data from graduate students """
        if tkMessageBox.askyesno('Verify', 'Really delete?'):
            print("Index: " + str(self._listbox.curselection()[0]))
            self._listbox.delete(tk.ANCHOR)
            return True
        return False

    def get_index(self):
        """ getting the student index """
        index = self._listbox.curselection()[0]
        return index