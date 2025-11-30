from config.db import get_connection

def update_expense():
    conn = get_connection()
    crs=conn.cursor()
    
    print("\n ====== UPDATE EXPENSE ======")

    try:
         id=int(input("Enter id of expense to  update data"))
    except ValueError:
        print("Invalid ID. Must be a number.")
        crs.close()
        conn.close()
        return

    crs.execute("select * from expense where id = %s",(id,))
    data=crs.fetchone()
    if data is None:
        print("Expense id not found")
        crs.close()
        conn.close()
        return


    print("\n Old Data:")
    print("Id          : ",data[0])
    print("Amount      : ",data[1])
    print("Category    : ",data[2])
    print("Description : ",data[3])
    print("Date        : ",data[4])

    print("\nWhat do you want to update?")
    print("1. Amount")
    print("2. Category")
    print("3. Description")
    print("4. Update All")
    print("5. Cancel")
    try:
        choice=int(input("Enter choice"))
    except:
        print("Invalid input. Must be a number 1-5.")
        crs.close()
        conn.close()
        return
    try:
        if choice==1:
            
            while True:
                
                 try:
                    new_amt=float(input("Enter new amount"))
                    if new_amt<=0:
                        print("Amount must be greater than Zero.Try Again..!")
                        continue
                    break
                 except ValueError:
                     print("Invalid input. Enter a number.")
            crs.execute("update expense set amt=%s where id=%s",(new_amt,id))

        elif choice ==2:
            new_cat=input("Enter new Category").strip()
            crs.execute("update expense set category=%s where id=%s",(new_cat,id))
        elif choice ==3:
            new_desc=input("Enter new Description").strip()
            crs.execute("update expense set description=%s where id=%s",(new_desc,id))
        elif choice ==4:
            while True:
                 
                 try:
                    new_amt=float(input("Enter new amount"))
                    if new_amt<=0:
                        print("Amount must be greater than Zero.Try Again..!")
                        continue
                    break
                 except ValueError:
                     print("amount must be number")
            new_cat=input("Enter new Category").strip()
            new_desc=input("Enter new Description").strip()
            crs.execute("update expense set amt=%s, category=%s , description=%s where id=%s",(new_amt,new_cat,new_desc,id))
        elif choice==5:
            print("Update cancelled.")
            crs.close()
            conn.close()
            return
        else:
            print("invalid choice..!")
            crs.close()
            conn.close()
            return
        conn.commit()
        print("Expense updated successfully!")
    except Exception as e:
        print("Error updating expense:", e)
    
    crs.close()
    conn.close()
        