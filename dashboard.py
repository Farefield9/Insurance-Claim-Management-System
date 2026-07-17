import tkinter as tk
import customer
import policy
import claims
import reports

def open_dashboard():

    dashboard = tk.Tk()

    dashboard.title("Insurance Claim Management System")
    dashboard.geometry("600x400")


    title = tk.Label(
        dashboard,
        text="Welcome Admin",
        font=("Arial",18,"bold")
    )

    title.pack(pady=40)


    customer_btn = tk.Button(
        dashboard,
        text="Customer Management",
        width=25,
        command=customer.open_customer
    )

    customer_btn.pack(pady=10)


    policy_btn = tk.Button(
    dashboard,
    text="Policy Management",
    width=25,
    command=policy.open_policy
    )

    policy_btn.pack(pady=10)


    claim_btn = tk.Button(
    dashboard,
    text="Claim Management",
    width=25,
    command=claims.open_claim
    )

    claim_btn.pack(pady=10)


    report_btn = tk.Button(
    dashboard,
    text="Reports",
    width=25,
    command=reports.open_reports
    )

    report_btn.pack(pady=10)


    dashboard.mainloop()
