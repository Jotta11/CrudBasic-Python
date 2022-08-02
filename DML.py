#DML
import sqlite3


def commit_close(func):
    def decorator(*args):
        con = sqlite3.connect('base.db')
        cur = con.cursor()
        sql = func(*args)
        cur.execute(sql)
        con.commit()
        con.close()
    return decorator   

            
@commit_close
def db_insert(name,phone,email):
    return """
    INSERT INTO users (name, phone, email)
     VALUES('{}', '{}', '{}')
     """.format(name,phone,email)

@commit_close
def db_update(name, email):
    return""" 
    UPDATE users SET name = '{}' WHERE email = '{}'
    """.format(name, email)

@commit_close
def db_delete(id):
    return"""
    DELETE FROM users WHERE id = '{}'
    """.format(id)

def db_select(data, field):
    return"""
     SELECT id, name, phone, email
     FROM users
     WHERE {} = {}
    """.format(field, data)
    #data = cur.fetchone()


