import tkinter as tk
from tkinter import ttk, messagebox
from db import get_connection



def add_claim():

    customer_id = customer_entry.get()
    policy_id = policy_entry.get()
    claim_date = date_entry.get()
    amount = amount_entry.get()
    reason = reason_entry.get()


    if customer_id == "" or policy_id == "":
        messagebox.showwarning(
            "Warning",
            "Customer ID and Policy ID required"
        )
        return


    conn = get_connection()
    cursor = conn.cursor()


    query = """
    INSERT INTO claims
    (customer_id, policy_id, claim_date, claim_amount, reason, status)
    VALUES (%s,%s,%s,%s,%s,%s)
    """


    cursor.execute(
        query,
        (
            customer_id,
            policy_id,
            claim_date,
            amount,
            reason,
            "Pending"
        )
    )


    conn.commit()
    conn.close()


    messagebox.showinfo(
        "Success",
        "Claim Submitted"
    )


    show_claims()





def show_claims():

    for row in table.get_children():
        table.delete(row)


    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT 
        claim_id,
        customer_id,
        policy_id,
        claim_date,
        claim_amount,
        reason,
        status
        FROM claims
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




def update_status(status):

    selected = table.focus()


    if selected == "":
        messagebox.showwarning(
            "Warning",
            "Select claim"
        )
        return


    data = table.item(selected)

    claim_id = data["values"][0]


    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        UPDATE claims
        SET status=%s
        WHERE claim_id=%s
        """,
        (
            status,
            claim_id
        )
    )


    conn.commit()
    conn.close()


    messagebox.showinfo(
        "Success",
        "Claim Status Updated"
    )


    show_claims()





def delete_claim():

    selected = table.focus()


    if selected == "":
        return


    data = table.item(selected)

    claim_id = data["values"][0]


    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        DELETE FROM claims
        WHERE claim_id=%s
        """,
        (claim_id,)
    )


    conn.commit()
    conn.close()


    show_claims()





def open_claim():

    global customer_entry
    global policy_entry
    global date_entry
    global amount_entry
    global reason_entry
    global table



    window = tk.Toplevel()

    window.title(
        "Claim Management"
    )

    window.geometry(
        "950x600"
    )



    tk.Label(
        window,
        text="Customer ID"
    ).grid(row=0,column=0)



    customer_entry=tk.Entry(window)

    customer_entry.grid(row=0,column=1)



    tk.Label(
        window,
        text="Policy ID"
    ).grid(row=1,column=0)



    policy_entry=tk.Entry(window)

    policy_entry.grid(row=1,column=1)




    tk.Label(
        window,
        text="Claim Date"
    ).grid(row=2,column=0)



    date_entry=tk.Entry(window)

    date_entry.grid(row=2,column=1)




    tk.Label(
        window,
        text="Claim Amount"
    ).grid(row=3,column=0)



    amount_entry=tk.Entry(window)

    amount_entry.grid(row=3,column=1)




    tk.Label(
        window,
        text="Reason"
    ).grid(row=4,column=0)



    reason_entry=tk.Entry(window)

    reason_entry.grid(row=4,column=1)





    add_btn=tk.Button(
        window,
        text="Submit Claim",
        command=add_claim
    )

    add_btn.grid(
        row=5,
        column=0,
        pady=20
    )



    approve_btn=tk.Button(
        window,
        text="Approve",
        command=lambda:update_status("Approved")
    )

    approve_btn.grid(
        row=5,
        column=1
    )



    reject_btn=tk.Button(
        window,
        text="Reject",
        command=lambda:update_status("Rejected")
    )

    reject_btn.grid(
        row=5,
        column=2
    )



    delete_btn=tk.Button(
        window,
        text="Delete",
        command=delete_claim
    )

    delete_btn.grid(
        row=5,
        column=3
    )





    columns=(
        "Claim ID",
        "Customer ID",
        "Policy ID",
        "Date",
        "Amount",
        "Reason",
        "Status"
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
        columnspan=5,
        pady=20
    )



    show_claims()
