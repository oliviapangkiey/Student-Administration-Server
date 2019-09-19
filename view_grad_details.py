import tkinter as tk
from tkinter import messagebox as tkMessageBox


class ViewGradDetails(tk.Frame):
    """ Add Popup Window """

    def __init__(self, parent, close_popup_callback, student):
        """ Initialize the nav bar """
        tk.Frame.__init__(self, parent)
        self._parent = parent
        self.grid(rowspan=5, columnspan=5, padx=20, pady=20)

        self._close_popup_callback = close_popup_callback
        self._student = student
        self._create_widgets()

    def _create_widgets(self):
        self._title = tk.Label(self, text='Student Details')
        self._title.grid(row=0, columnspan=3)

        self._first_name = tk.Label(self, text="First Name:    ").grid(row=1, column=0)
        self._first_name_value = tk.Label(self, text = self._student['first_name']).grid(row=1, column = 1)
        self._last_name = tk.Label(self, text="Last Name:   ").grid(row=2, column=0)
        self._last_name_value = tk.Label(self, text=self._student['last_name']).grid(row=2, column=1)
        self._program = tk.Label(self, text="Program:   ").grid(row=3, column=0)
        self._program_value = tk.Label(self, text=self._student['program']).grid(row=3, column=1)
        self._classification = tk.Label(self, text="Classification: ").grid(row=4, column=0)
        self._classification_value = tk.Label(self, text=self._student['classification']).grid(row=4, column=1)
        self._enroll_status = tk.Label(self, text="Enroll status:   ").grid(row=5, column=0)
        self._estatus_value = tk.Label(self, text=self._student['enroll_status']).grid(row=5, column=1)
        self._enroll_date = tk.Label(self, text="Enroll date:   ").grid(row=6, column=0)
        self._edate_value = tk.Label(self, text=self._student['enroll_date']).grid(row=6, column=1)
        self._type = tk.Label(self, text="Type: ").grid(row =7, column = 0)
        self._type_value = tk.Label(self, text=self._student['type']).grid(row=7, column=1)
        self._supervisor = tk.Label(self, text="Supervisor: ").grid(row=8, column=0)
        self._supervisor_value = tk.Label(self, text=self._student['supervisor']).grid(row=8, column=1)
        self._undergrad_degree = tk.Label(self, text="Undergraduate degree: ").grid(row=9, column=0)
        self._undergraddegree_value = tk.Label(self, text=self._student['undergraduate_degree']).grid(row=9, column=1)


        self._button2 = tk.Button(self,
                                  text="Close",
                                  command=self._close_popup_callback).grid(row=10, column=1)
