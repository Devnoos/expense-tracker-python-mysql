from config.db import get_connection

def view_expenses():
    conn=get_connection()
    crs=conn.cursor()

    

    crs.execute("select * from expense")
    rows=crs.fetchall()

    if len(rows)==0:
        print("No Expenses found")
        crs.close()
        conn.close()
        return

    else:
        print("\n =====ALL EXPENSES=====")
        print(f"{'ID':<5}{'Amount':<10}{'Category':<15}{'Description':<30}{'Date':<12}")
        print("-"*80)
        for i in rows:
             print(f"{i[0]:<5}{i[1]:<10}{i[2]:<15}{i[3]:<30}{i[4]}")
    crs.close()
    conn.close()
