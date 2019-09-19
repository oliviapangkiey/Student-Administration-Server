import tkinter as tk
from tkinter import messagebox as tkMessageBox




class AddGradPopup(tk.Frame):
    """ Add Popup Window """

    def __init__(self, parent, close_popup_callback, add_button):
        """ Initialize the nav bar """
        tk.Frame.__init__(self, parent)
        self._parent = parent
        self.grid(rowspan=5, columnspan=5, padx=20, pady=20)

        self._close_popup_callback = close_popup_callback
        self._add_button = add_button
        self._create_widgets()

    def _create_widgets(self):
        self._title = tk.Label(self, text='Add Graduate Student')
        self._title.grid(row=1, columnspan=3)

        self._first_name = tk.Label(self, text="First Name").grid(row=2, column=0)
        self._last_name = tk.Label(self, text="Last Name").grid(row=3, column=0)
        self._program = tk.Label(self, text="Program").grid(row=4, column=0)
        self._classification = tk.Label(self, text="Classification").grid(row=5, column=0)
        self._enroll_status = tk.Label(self, text="Enroll status").grid(row=6, column=0)
        self._enroll_date = tk.Label(self, text="Enroll date").grid(row=7, column=0)
        # self._type = tk.Label(self, text="Type").grid(row=8, column=0)
        self._supervisor = tk.Label(self, text="Supervisor").grid(row=9, column=0)
        self._undergrad_degree = tk.Label(self, text="Undergraduate Degree").grid(row=10, column=0)

        self.e_first_name = tk.Entry(self)
        self.e_first_name.grid(row=2, column=1)
        self.e_last_name = tk.Entry(self)
        self.e_last_name.grid(row=3, column=1)
        self.e_program = tk.Entry(self)
        self.e_program.grid(row=4, column=1)
        self.e_classification = tk.Entry(self)
        self.e_classification.grid(row=5, column=1)
        self.e_enroll_status = tk.Entry(self)
        self.e_enroll_status.grid(row=6, column=1)
        self.e_enroll_date = tk.Entry(self)
        self.e_enroll_date.grid(row=7, column=1)
        # self.e_type = tk.Entry(self)
        # self.e_type.grid(row=8, column=1)
        self.e_supervisor = tk.Entry(self)
        self.e_supervisor.grid(row=9, column=1)
        self.e_undergrad_degree = tk.Entry(self)
        self.e_undergrad_degree.grid(row=10, column=1)

        tk.Button(self,
                  text="Submit",
                  command=self._add_button).grid(row=11, column=0)

        tk.Button(self,
                  text="Close",
                  command=self._close_popup_callback).grid(row=11, column=1)


    def get_data(self):
        """ mapping the data into dictionary """
        data = {"first_name": self.e_first_name.get(),
                "last_name": self.e_last_name.get(),
                "program": self.e_program.get(),
                "classification": self.e_classification.get(),
                "enroll_status": self.e_enroll_status.get(),
                "enroll_date": self.e_enroll_date.get(),
                "type": "Graduate",
                "supervisor": self.e_supervisor.get(),
                "undergraduate_degree": self.e_undergrad_degree.get()}
        return data

    def message_box(self, status_code):
        """ shows message box after pressing the add button """
        if status_code == 200:
            tkMessageBox.showinfo("Success", "Student record is added!")
        else:
            tkMessageBox.showerror("Error", "Student is invalid or missing data.")