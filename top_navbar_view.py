import tkinter as tk


class TopNavbarView(tk.Frame):

    # DISPLAY_ALL = 1
    UNDERGRADUATE = 1
    GRADUATE = 2

    def __init__(self, parent, page_callback):
        tk.Frame.__init__(self, parent)
        self._parent = parent

        self._page_callback = page_callback

        self._page = tk.IntVar()
        self._create_widgets()


    def _create_widgets(self):
        tk.Label(self,
                 text="Student Manager").grid(row=0, column=2)

        tk.Label(self,
                 text="Display:").grid(row=1, column=0)

        self.curr_page = tk.IntVar()

        # tk.Radiobutton(self,
        #                text="All",
        #                variable=self.curr_page,
        #                command=self._page_callback,
        #                value=TopNavbarView.DISPLAY_ALL).grid(row=1, column=1)
        tk.Radiobutton(self,
                       text="Undergraduate",
                       variable=self.curr_page,
                       command=self._page_callback,
                       value=TopNavbarView.UNDERGRADUATE).grid(row=1, column=2)
        tk.Radiobutton(self,
                       text="Graduate",
                       variable=self.curr_page,
                       command=self._page_callback,
                       value=TopNavbarView.GRADUATE).grid(row=1, column=3)



        self.curr_page.set(TopNavbarView.UNDERGRADUATE)
        self._page.set(1)
