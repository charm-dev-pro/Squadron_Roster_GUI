import sqlite3

conn = sqlite3.connect('squadron_roster_3.db')
cur = conn.cursor()

# for row in cur.execute("SELECT * FROM CADETS"):
# print(row)
#cur.execute("INSERT INTO CADETS (CAPID, FIRST_NAME, LAST_NAME, RANK) VALUES (2, 'Jim', 'JOm', 'C/Amn')")
#for row in cur.execute("SELECT * FROM CADETS"):
    #print(row)

#for row in cur.execute("SELECT * FROM ROSTER"):
    #print(row)

#cur.execute("DELETE FROM CADETS WHERE CAPID = 11")
for row in cur.execute("SELECT * FROM CADETS"):
    print(row)

