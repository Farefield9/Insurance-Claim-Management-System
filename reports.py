import tkinter as tk
from tkinter import ttk, messagebox
from db import get_connection
import pandas as pd



def export_customers():

    conn = get_connection()

    query = """
    SELECT *
    FROM customers
    """

    df = pd.read_sql(
        query,
        conn
    )

    df.to_csv(
        "customers_report.csv",
        index=False
    )

    conn.close()


    messagebox.showinfo(
        "Success",
        "Customer report exported"
    )





def export_claims():

    conn = get_connection()

    query = """
    SELECT *
    FROM claims
    """

    df = pd.read_sql(
        query,
        conn
    )


    df.to_csv(
        "claims_report.csv",
        index=False
    )


    conn.close()


    messagebox.showinfo(
        "Success",
        "Claim report exported"
    )





def view_summary():

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT 
        status,
        COUNT(*)
        FROM claims
        GROUP BY status
        """
    )


    data = cursor.fetchall()


    conn.close()


    for row in summary_table.get_children():
        summary_table.delete(row)


    for row in data:
        summary_table.insert(
            "",
            tk.END,
            values=row
        )





def open_reports():

    global summary_table


    window = tk.Toplevel()

    window.title(
        "Reports"
    )

    window.geometry(
        "600x400"
    )



    title=tk.Label(
        window,
        text="Insurance Reports",
        font=("Arial",18,"bold")
    )

    title.pack(
        pady=20
    )



    customer_btn=tk.Button(
        window,
        text="Export Customer Report",
        command=export_customers
    )

    customer_btn.pack(
        pady=10
    )



    claim_btn=tk.Button(
        window,
        text="Export Claim Report",
        command=export_claims
    )


    claim_btn.pack(
        pady=10
    )



    summary_btn=tk.Button(
        window,
        text="Claim Summary",
        command=view_summary
    )


    summary_btn.pack(
        pady=10
    )



    columns=(
        "Status",
        "Count"
    )


    summary_table=ttk.Treeview(
        window,
        columns=columns,
        show="headings"
    )


    for col in columns:
        summary_table.heading(
            col,
            text=col
        )


    summary_table.pack(
        pady=20
    )
