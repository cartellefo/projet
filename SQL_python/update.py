import psycopg2

 
def update_vendor(vendor_id, vendor_name):
    """ update vendor name based on the vendor id """
    sql = """ UPDATE vendors
                SET vendor_name = %s
                WHERE vendor_id = %s"""
    conn = None
    updated_rows = 0
    try:
       
        conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='dbpass'")
        
        cur = conn.cursor()
       
        cur.execute(sql, (vendor_name, vendor_id))
        
        updated_rows = cur.rowcount
        
        conn.commit()
        
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return updated_rows