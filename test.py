import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont

class ColoredEntry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(borderwidth="1px")
        ft = tkFont.Font(family='Helvetica', size=13)
        self.configure(font=ft, fg="#273746", justify="left")

class ColoredButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(bg="#ADD8E6")
        ft = tkFont.Font(family='Helvetica', size=14)
        self.configure(font=ft, fg="#000000", justify="center")

class App:
    def __init__(self, root):
        root.title("Ứng Dụng Quản Lý Thư Viện")
        root.configure(bg="#E5E5E5")
        width = 990
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % ((width, height, (screenwidth - width) / 2, (screenheight - height) / 2))
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.tree = ttk.Treeview(root, columns=("Mã Sách", "Tên Sách", "Thể Loại","Tác Giả", "Ngày Xuất Bản"), show="headings")
        self.tree.heading("Mã Sách", text="Mã Sách")
        self.tree.heading("Tên Sách", text="Tên Sách")
        self.tree.heading("Thể Loại", text="Thể Loại")
        self.tree.heading("Tác Giả", text="Tác Giả")
        self.tree.heading("Ngày Xuất Bản", text="Ngày Xuất Bản")
        self.tree.column("Mã Sách", width=100, anchor="center")
        self.tree.column("Tên Sách", width=100)
        self.tree.column("Thể Loại", width=80)
        self.tree.column("Tác Giả", width=100)
        self.tree.column("Ngày Xuất Bản", width=100, anchor="center")
        self.tree.place(x=380, y=50, width=576, height=322)

        self.label_student_id = tk.Label(root, text="Mã Sách:", bg="#E5E5E5", fg="#273746")
        self.label_student_id.place(x=40, y=50, width=47, height=31)
        self.entry_student_id = ColoredEntry(root)
        self.entry_student_id.place(x=160, y=50, width=194, height=31)

        self.label_student_name = tk.Label(root, text="Tên Sách:", bg="#E5E5E5", fg="#273746")
        self.label_student_name.place(x=40, y=100, width=53, height=32)
        self.entry_student_name = ColoredEntry(root)
        self.entry_student_name.place(x=160, y=100, width=194, height=32)

        self.label_student_category = tk.Label(root, text="Thể Loại:", bg="#E5E5E5", fg="#273746")
        self.label_student_category.place(x=40, y=150, width=53, height=32)
        self.entry_student_category = ColoredEntry(root)
        self.entry_student_category.place(x=160, y=150, width=194, height=32)

        self.label_student_author = tk.Label(root, text="Tác Giả", bg="#E5E5E5", fg="#273746")
        self.label_student_author.place(x=40, y=200, width=53, height=32)
        self.entry_student_author = ColoredEntry(root)
        self.entry_student_author.place(x=160, y=200, width=194, height=32)

        self.label_student_dob = tk.Label(root, text="Ngày XB:", bg="#E5E5E5", fg="#273746")
        self.label_student_dob.place(x=40, y=250, width=70, height=38)
        self.entry_student_dob = ColoredEntry(root)
        self.entry_student_dob.place(x=160, y=250, width=194, height=32)

        self.button_add = ColoredButton(root, text="Thêm", command=self.add_student)
        self.button_add.place(x=50, y=390, width=170, height=48)

        self.button_edit = ColoredButton(root, text="Sửa", command=self.edit_student)
        self.button_edit.place(x=250, y=390, width=165, height=47)

        self.button_sort = ColoredButton(root, text="Sắp xếp", command=self.show_sort_menu)
        self.button_sort.place(x=440, y=390, width=161, height=47)

        self.button_delete = ColoredButton(root, text="Xóa", command=self.delete_student)
        self.button_delete.place(x=630, y=390, width=153, height=46)

        self.button_exit = ColoredButton(root, text="Thoát", command=root.quit)
        self.button_exit.place(x=830, y=390, width=100, height=46)

        label_title = tk.Label(root, text="ỨNG DỤNG QUẢN LÝ THƯ VIỆN ", font=("Helvetica", 18, "bold"), fg="#FFA500", bg="#E5E5E5")
        label_title.place(x=200, y=10, width=582, height=30)

        self.sort_menu = tk.Menu(root, tearoff=0)
        self.sort_menu.add_command(label="Sắp xếp theo Mã Sách", command=lambda: self.sort_students_ID())
        self.sort_menu.add_command(label="Sắp xếp theo Tên Sách", command=lambda: self.sort_students_name())
        self.sort_menu.add_command(label="Sắp xếp theo Thể Loại", command=lambda: self.sort_students_category())
        self.sort_menu.add_command(label="Sắp xếp theo Tác Giả", command=lambda: self.sort_students_author())
        self.sort_menu.add_command(label="Sắp xếp theo Ngày XB", command=lambda: self.sort_students_dob())

    def edit_student(self):
        selected_items = self.tree.selection()
        if selected_items:
            selected_item = selected_items[0]
            student_info = self.tree.item(selected_item, "values")

            edit_window = tk.Toplevel()
            edit_window.title("Sửa Thông Tin Sách")
            edit_window.geometry("300x250")

            label_id = tk.Label(edit_window, text="Mã Sách:")
            label_id.pack()
            entry_id = ColoredEntry(edit_window)
            entry_id.pack()
            entry_id.insert(0, student_info[0])

            label_name = tk.Label(edit_window, text="Tên Sách:")
            label_name.pack()
            entry_name = ColoredEntry(edit_window)
            entry_name.pack()
            entry_name.insert(0, student_info[1])

            label_category = tk.Label(edit_window, text="Thể Loại:")
            label_category.pack()
            entry_category = ColoredEntry(edit_window)
            entry_category.pack()
            entry_category.insert(0, student_info[2])

            label_author = tk.Label(edit_window, text="Tác Giả:")
            label_author.pack()
            entry_author = ColoredEntry(edit_window)
            entry_author.pack()
            entry_author.insert(0, student_info[3])

            label_dob = tk.Label(edit_window, text="Ngày XB:")
            label_dob.pack()
            entry_dob = ColoredEntry(edit_window)
            entry_dob.pack()
            entry_dob.insert(0, student_info[4])

            button_save = ColoredButton(edit_window, text="Lưu", command=lambda: self.save_edited_info(edit_window, selected_item, entry_id, entry_name, entry_category, entry_author, entry_dob))
            button_save.pack()

    def save_edited_info(self, edit_window, selected_item, entry_id, entry_name, entry_category, entry_author, entry_dob):
        new_id = entry_id.get()
        new_name = entry_name.get()
        new_category = entry_category.get()
        new_author = entry_author.get()
        new_dob = entry_dob.get()

        self.tree.item(selected_item, values=(new_id, new_name, new_category, new_author, new_dob))

        edit_window.destroy()

    def show_sort_menu(self):
        self.sort_menu.post(self.button_sort.winfo_rootx(), self.button_sort.winfo_rooty() + self.button_sort.winfo_height())

    def add_student(self):
        student_id = self.entry_student_id.get()
        student_name = self.entry_student_name.get()
        student_category = self.entry_student_category.get()
        student_author = self.entry_student_author.get()
        student_dob = self.entry_student_dob.get()

        self.tree.insert("", tk.END, values=(student_id, student_name, student_category, student_author, student_dob))

        self.entry_student_id.delete(0, tk.END)
        self.entry_student_name.delete(0, tk.END)
        self.entry_student_category.delete(0, tk.END)
        self.entry_student_author.delete(0, tk.END)
        self.entry_student_dob.delete(0, tk.END)

    def sort_students_ID(self):
        initial_stt = {child: int(self.tree.item(child, "values")[0]) for child in self.tree.get_children("")}
        data = [(self.tree.set(child, "Mã Sách"), child) for child in self.tree.get_children("")]
        data.sort()

        for index, item in enumerate(data):
            self.tree.move(item[1], "", index)
            stt = initial_stt[item[1]]
            self.tree.item(item[1], values=(stt,) + self.tree.item(item[1], "values")[1:])

        self.tree.heading("Mã Sách", command=lambda: self.treeview_sort_column(self.tree, "Mã Sách", False))

    def sort_students_name(self):
        initial_stt = {child: int(self.tree.item(child, "values")[0]) for child in self.tree.get_children("")}
        data = [(self.tree.set(child, "Tên Sách"), child) for child in self.tree.get_children("")]
        data.sort()

        for index, item in enumerate(data):
            self.tree.move(item[1], "", index)
            stt = initial_stt[item[1]]
            self.tree.item(item[1], values=(stt,) + self.tree.item(item[1], "values")[1:])

        self.tree.heading("Tên Sách", command=lambda: self.treeview_sort_column(self.tree, "Tên Sách", False))

    def sort_students_category(self):
        initial_stt = {child: int(self.tree.item(child, "values")[0]) for child in self.tree.get_children("")}
        data = [(self.tree.set(child, "Thể Loại"), child) for child in self.tree.get_children("")]
        data.sort()

        for index, item in enumerate(data):
            self.tree.move(item[1], "", index)
            stt = initial_stt[item[1]]
            self.tree.item(item[1], values=(stt,) + self.tree.item(item[1], "values")[1:])

        self.tree.heading("Thể Loại", command=lambda: self.treeview_sort_column(self.tree, "Thể Loại", False))

    def sort_students_author(self):
        initial_stt = {child: int(self.tree.item(child, "values")[0]) for child in self.tree.get_children("")}
        data = [(self.tree.set(child, "Tác Giả"), child) for child in self.tree.get_children("")]
        data.sort()

        for index, item in enumerate(data):
            self.tree.move(item[1], "", index)
            stt = initial_stt[item[1]]
            self.tree.item(item[1], values=(stt,) + self.tree.item(item[1], "values")[1:])

        self.tree.heading("Tác Giả", command=lambda: self.treeview_sort_column(self.tree, "Tác Giả", False))

    def sort_students_dob(self):
        initial_stt = {child: int(self.tree.item(child, "values")[0]) for child in self.tree.get_children("")}
        data = [(self.tree.set(child, "Ngày Xuất Bản"), child) for child in self.tree.get_children("")]
        data.sort()

        for index, item in enumerate(data):
            self.tree.move(item[1], "", index)
            stt = initial_stt[item[1]]
            self.tree.item(item[1], values=(stt,) + self.tree.item(item[1], "values")[1:])

        self.tree.heading("Ngày Xuất Bản", command=lambda: self.treeview_sort_column(self.tree, "Ngày Xuất Bản", False))

    def delete_student(self):
        selected_items = self.tree.selection()
        if selected_items:
            for item in selected_items:
                self.tree.delete(item)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
