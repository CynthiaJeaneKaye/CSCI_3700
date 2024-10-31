from flask import Flask, render_template
import util


app = Flask(__name__)

# evil global variables
username='raywu1990'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'


@app.route('/api/update_basket_a')
def update():
    # connect to DB
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    
    # execute SQL commands
    record = util.run_and_fetch_sql(cursor, "insert into basket_a (a, fruit_a) values (5,'Cherry');")
    
    if isinstance(record, list):
        return 'Success~!'

    # disconnect from database
    util.disconnect_from_db(connection,cursor)
    	
    return record
      

@app.route('/api/unique')
def unique():
    # connect to DB
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    
    # execute SQL commands
    record = util.run_and_fetch_sql(cursor, "select a, fruit_a, b, fruit_b from basket_a full join basket_b on fruit_a = fruit_b where a is null or b is null;")
        
    
    if isinstance(record, list):
        col_names = [desc[0] for desc in cursor.description]
        log = record[:5]
        return render_template('index.html', sql_table = log, table_title=col_names)
    	
    # disconnect from database
    util.disconnect_from_db(connection,cursor)
    
    return record


if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)

