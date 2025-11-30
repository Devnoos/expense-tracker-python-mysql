from config.db import get_connection
def add_expense():
    conn=get_connection()
    crs=conn.cursor()

    print("\n =====ADD EXPENSE=====")
    category=input("Enter Category").strip()
    Description=input("Enter Description of Expense").strip()
    while True:
        try:
            amount=float(input("Enter Amount"))
            if amount<=0:
                print("Amount must be greater than Zero.Try Again..!")
                continue
            break
        except ValueError:
            print("invalid input! Enter numeric value")
    
    insert_query="insert into expense (amt,category,description) values(%s,%s,%s)"
    values=(amount,category,Description)
    crs.execute(insert_query,values)
    conn.commit()

    print("Expense added successfully ")
    crs.close()
    conn.close()

        