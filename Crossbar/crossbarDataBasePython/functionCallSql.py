import psycopg2
import sys
for eachArg in sys.argv:   
    print(eachArg)
#import sys
#for arg in sys.argv:
    #print(arg)
conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='dbpass'")
cur = conn.cursor()

#cur.execute("""select vendors_number()""")

p_max= int(sys.argv[1])
#print(p_max)
cur.execute("""select players_young(%s)""",[p_max])
#cur.execute("""select players_young("""+p_max+""")""")
x= cur.fetchone()[0]
#y = cur.fetchone()[0]
print(x)
#print(y)

#cursor.execute("INSERT INTO table VALUES (%s, %s, %s)", (var1, var2, var3))
