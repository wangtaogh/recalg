import sqlite3
con=sqlite3.connect("d:\sales.db")
#con.execute("create table region(id primary key,name)")
#regions=[('021','上海'),('022','天津'),('023','重庆'),('024','沈阳')]
#con.execute("insert into region(id,name) values('020','广东')")
#con.execute("insert into region(id,name) values(?,?)",('010','北京'))
#con.executemany("insert into region(id,name) values(?,?)",regions)
#con.execute("update region set name=? where id=?",('广州','020'))
n=con.execute("delete from region where id=?",('024',))
print('删除了',n.rowcount,'行记录')
con.commit()
#con.close()
cur=con.execute("select id,name from region")
for row in cur:
    print(row)
con.close()
