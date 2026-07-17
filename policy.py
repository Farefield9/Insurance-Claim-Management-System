import tkinter as tk
from tkinter import ttk, messagebox
from db import get_connection


def add_policy():

    customer_id = customer_id_entry.get()
    policy_type = policy_type_entry.get()
    premium = premium_entry.get()
    start_date = start_entry.get()
    end_date = end_entry.get()


    if customer_id == "" or policy_type == "":
        messagebox.showwarning(
            "Warning",
            "Customer ID and Policy Type required"
        )
        return


    conn = get_connection()
    cursor = conn.cursor()


    query = """
    INSERT INTO policies
    (customer_id, policy_type, premium, start_date, end_date)
    VALUES (%s,%s,%s,%s,%s)
    """


    cursor.execute(
        query,
        (
            customer_id,
            policy_type,
            premium,
            start_date,
            end_date
        )
    )


    conn.commit()
    conn.close()


    messagebox.showinfo(
        "Success",
        "Policy Added Successfully"
    )


    show_policies()



def show_policies():

    for row in table.get_children():
        table.delete(row)


    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT 
        policy_id,
        customer_id,
        policy_type,
        premium,
        start_date,
        end_date
        FROM policies
        """
    )


    rows = cursor.fetchall()


    for row in rows:
        table.insert(
            "",
            tk.END,
            values=row
        )


    conn.close()



def delete_policy():

    selected = table.focus()

    if selected == "":
        messagebox.showwarning(
            "Warning",
            "Select policy"
        )
        return


    data = table.item(selected)

    policy_id = data["values"][0]


    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        """
        DELETE FROM policies
        WHERE policy_id=%s
        """,
        (policy_id,)
    )


    conn.commit()
    conn.close()


    messagebox.showinfo(
        "Success",
        "Policy Deleted"
    )


    show_policies()




def open_policy():

    global customer_id_entry
    global policy_type_entry
    global premium_entry
    global start_entry
    global end_entry
    global table


    window = tk.Toplevel()

    window.title(
        "Policy Management"
    )

    window.geometry(
        "850x500"
    )


    # Customer ID

    tk.Label(
        window,
        text="Customer ID"
    ).grid(
        row=0,
        column=0,
        padx=10,
        pady=10
    )


    customer_id_entry=tk.Entry(window)

    customer_id_entry.grid(
        row=0,
        column=1
    )


    # Policy Type

    tk.Label(
        window,
        text="Policy Type"
    ).grid(
        row=1,
        column=0
    )


    policy_type_entry=tk.Entry(window)

    policy_type_entry.grid(
        row=1,
        column=1
    )



    # Premium

    tk.Label(
        window,
        text="Premium Amount"
    ).grid(
        row=2,
        column=0
    )


    premium_entry=tk.Entry(window)

    premium_entry.grid(
        row=2,
        column=1
    )



    # Start Date

    tk.Label(
        window,
        text="Start Date"
    ).grid(
        row=3,
        column=0
    )


    start_entry=tk.Entry(window)

    start_entry.grid(
        row=3,
        column=1
    )



    # End Date

    tk.Label(
        window,
        text="End Date"
    ).grid(
        row=4,
        column=0
    )


    end_entry=tk.Entry(window)

    end_entry.grid(
        row=4,
        column=1
    )



    add_button=tk.Button(
        window,
        text="Add Policy",
        command=add_policy
    )

    add_button.grid(
        row=5,
        column=0,
        pady=20
    )



    delete_button=tk.Button(
        window,
        text="Delete Policy",
        command=delete_policy
    )

    delete_button.grid(
        row=5,
        column=1
    )



    columns=(
        "Policy ID",
        "Customer ID",
        "Policy Type",
        "Premium",
        "Start Date",
        "End Date"
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
        row=6,
        column=0,
        columnspan=4,
        pady=20
    )


    show_policies()
