from config.db import get_connection

def total_expense():
    conn= get_connection()
    crs=conn.cursor()
    print("\n TOTAL EXPENSE ")
    crs.execute("select sum(amt) from expense")
    total=crs.fetchone()[0]
    if total is None:
        print("No Expenses record yet")
        crs.close()
        conn.close()
        return

    else:
        print(f"Total expense : {total}")
    crs.close()
    conn.close()
            