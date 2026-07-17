import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from db import get_connection



def add_customer():

    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()


    if name == "" or phone == "":
        messagebox.showwarning(
            "Warning",
            "Name and Phone required"
        )
        return


    conn = get_connection()

    cursor = conn.cursor()


    query = """
    INSERT INTO customers
    (name, phone, email, address)
    VALUES (%s,%s,%s,%s)
    """


    cursor.execute(
        query,
        (
            name,
            phone,
            email,
            address
        )
    )


    conn.commit()

    conn.close()


    messagebox.showinfo(
        "Success",
        "Customer Added"
    )


    clear_fields()
    show_customers()



def show_customers():

    for row in table.get_children():
        table.delete(row)


    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        "SELECT * FROM customers"
    )


    rows = cursor.fetchall()


    for row in rows:
        table.insert(
            "",
            tk.END,
            values=row
        )


    conn.close()



def delete_customer():

    selected = table.focus()

    if selected == "":
        messagebox.showwarning(
            "Warning",
            "Select customer"
        )
        return


    data = table.item(selected)

    customer_id = data["values"][0]


    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        "DELETE FROM customers WHERE customer_id=%s",
        (customer_id,)
    )


    conn.commit()

    conn.close()


    messagebox.showinfo(
        "Success",
        "Customer Deleted"
    )


    show_customers()



def clear_fields():

    name_entry.delete(0,tk.END)
    phone_entry.delete(0,tk.END)
    email_entry.delete(0,tk.END)
    address_entry.delete(0,tk.END)





def open_customer():

    global name_entry
    global phone_entry
    global email_entry
    global address_entry
    global table



    window = tk.Toplevel()

    window.title(
        "Customer Management"
    )

    window.geometry(
        "800x500"
    )



    tk.Label(
        window,
        text="Customer Name"
    ).grid(row=0,column=0,padx=10,pady=10)


    name_entry=tk.Entry(window)

    name_entry.grid(
        row=0,
        column=1
    )



    tk.Label(
        window,
        text="Phone"
    ).grid(row=1,column=0)



    phone_entry=tk.Entry(window)

    phone_entry.grid(
        row=1,
        column=1
    )



    tk.Label(
        window,
        text="Email"
    ).grid(row=2,column=0)


    email_entry=tk.Entry(window)

    email_entry.grid(
        row=2,
        column=1
    )



    tk.Label(
        window,
        text="Address"
    ).grid(row=3,column=0)


    address_entry=tk.Entry(window)

    address_entry.grid(
        row=3,
        column=1
    )



    add_btn=tk.Button(
        window,
        text="Add Customer",
        command=add_customer
    )

    add_btn.grid(
        row=4,
        column=0,
        pady=20
    )


    delete_btn=tk.Button(
        window,
        text="Delete Customer",
        command=delete_customer
    )

    delete_btn.grid(
        row=4,
        column=1
    )



    columns=(
        "ID",
        "Name",
        "Phone",
        "Email",
        "Address"
    )


    table=ttk.Treeview(
        window,
        columns=columns,
        show="headings"
    )


    for col in columns:
        table.heading(
            col,
            text=col
        )


    table.grid(
        row=5,
        column=0,
        columnspan=4,
        pady=20
    )


    show_customers()
