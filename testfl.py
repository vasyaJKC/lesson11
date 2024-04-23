import psycopg2

name = "Vasya"
last_name = "BlFms"
age = 17

data_base = psycopg2.connect(
    host='rain.db.elephantsql.com',
    user='givgaswx',
    database='givgaswx',
    password='93EGzftSqIGxAG5GpwkHCQjYuTBa66V3'
)
cursor = data_base.cursor()
cursor.execute(f"""INSERT INTO test_bot(name, last_name, age) values ('{name}', '{last_name}', {age})""")
cursor.execute("""Select * from test_bot""")
data = cursor.fetchall()
data_base.commit()
print(data)
