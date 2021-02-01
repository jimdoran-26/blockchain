from app import mysql, session

class Table():
    def __init__(self,table_name, *args):
        self.table = table_name
        self.columns = "(%s)"%",".join(args)

        if isNewtable(table_name):
            cur = mysql.connection.cursor()
            cur.execute("CREATE TABLE %s%s" %(self.table, self.columns))
            cur.close()

        # get all the values from the table
        def getall(self):
            cur = mysql.connection.cursor()
            result = cur.execute("SELECT * FROM %s" % self.table)
            data = cur.fetchall();
            return data

        # get one value from the table based on a column's data
        # EXAMPLE using blockchain: ...getone("hash","00003f73gh93...")
        def getone(self, search, value):
            data = {};
            cur = mysql.connection.cursor()
            result = cur.execute("SELECT * FROM %s WHERE %s = \"%s\"" % (self.table, search, value))
            if result > 0: data = cur.fetchone()
            cur.close();
            return data

        # delete a value from the table based on column's data
        def deleteone(self, search, value):
            cur = mysql.connection.cursor()
            cur.execute("DELETE from %s where %s = \"%s\"" % (self.table, search, value))
            mysql.connection.commit();
            cur.close()

        # delete all values from the table.
        def deleteall(self):
            self.drop()  # remove table and recreate
            self.__init__(self.table, *self.columnsList)

        # remove table from mysql
        def drop(self):
            cur = mysql.connection.cursor()
            cur.execute("DROP TABLE %s" % self.table)
            cur.close()

        # insert values into the table
        def insert(self, *args):
            data = ""
            for arg in args:  # convert data into string mysql format
                data += "\"%s\"," % (arg)

            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO %s%s VALUES(%s)" % (self.table, self.columns, data[:len(data) - 1]))
            mysql.connection.commit()
            cur.close()

def isNewtable(tableName):
    cur = mysql.connection.cursor()

    try: #attempt to get data from table
        result = cur.execute("SELECT * from %s" %tableName)
        cur.close()
    except:
        return True
    else:
        return False

users = Table("users","name","username","email","password")