import psycopg2
import sys
for eachArg in sys.argv:   
    print(eachArg)

# conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='dbpass'")
# cur = conn.cursor()
# p_max = int(sys.argv[1])
# #print(p_max)
# cur.execute("""select players_young(%s)""",[p_max])
# x = cur.fetchone()[0]
# print(x)



#cursor.execute("INSERT INTO table VALUES (%s, %s, %s)", (var1, var2, var3))
#cur.execute("""sSELECT * FROM sum_n_product_with_animal(2)""")

# x= int(sys.argv[1])
# y= int(sys.argv[2])
# z= int(sys.argv[3])
# conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='dbpass'")
# cur = conn.cursor()
# cur.execute("""SELECT * FROM sum_n_product_with_animal(%s,%s,%s)""",(x,y,z))
# x= cur.fetchall()[0]
# print(x)


s = 'Километр'
print(s.lower())
print(s.swapcase())
#print(s.decode('utf-8').lower())
