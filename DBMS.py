import sqlite3
import traceback

try:
    base = sqlite3.connect('CocksBase.bd')
    cockBD = base.cursor()
    print('DBMS fucked da faggots')
except:
    print('DBMS jerck off')

def inputQuery():
    query = ''
    queryType = 0

    while query.lower() != 'exit':
        queryType = input("1. Select\n2. Update\n3. Help\n")        

        if queryType == '1':
            select()
        elif queryType == '2':
            update()
        elif queryType == '3':
            help()
        else:
            return

    return


def format(msg):
	msg = str(msg)
	for simbol in msg:
		if simbol == ',' or simbol == '(' or simbol == ')':
			msg = msg.replace(simbol, '')
	return msg

def select():
    query = input("Query:\n")
    try:       
        cockBD.execute(query)
        selects = cockBD.fetchall()
        count = 0
        for select in selects:
            select = format(select)
            count += 1
            print('{}. {} \n'.format(count, select))

    except Exception as e:
        print('\nError:\n', traceback.format_exc(), '\n')

def update():
    query = input("Query:\n")
    try:
        cockBD.execute(query)
        base.commit()
        print("Update finished successfully")
    except Exception as e:
        base.rollback()
        print('\nError:\n', traceback.format_exc(), '\n')

def help():
    doc = """
    PRAGMA table_info(table_name) - table info
    
    """
    print(doc)

inputQuery()
