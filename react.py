import json
import jwt
import mysql.connector


def lambda_handler(event, context):
    
    def mysqlauth():
        return mysql.connector.connect(host="database-1.csao36671tpd.us-east-1.rds.amazonaws.com", user="groot", password="JbEPGE73ECAp5FG6SbELnNaPUGbuDj0AxcGQ", database="tnstorage")
    
    
    def decode(thing):
        mydb = mysqlauth()
        cursor = mydb.cursor()
        key = "secrete"
        encoded = thing
        decode = jwt.decode(encoded, key, algorithms="HS256")
        query = 'SELECT First_name, Last_name, DOB FROM penut_humanstorage WHERE id_number= '
        bob = decode['id_number']
        query = query + bob
        try:
            cursor.execute(query)
            data = cursor.fetchall()
            out = 'Confirmed:' + str(data[0][0]) + ', ' + str(data[0][1]) + ' ' + str(data[0][2])
        except IndexError:
            out = 'invalid please try again'
        return out
    ww = event.get("body")
    ww = ww.replace('name', '').replace('{', '').replace('}', '').replace(':', '').replace('"', '')
    print(ww)
    try:
        the = decode(ww)
    except:
        the = 'invalid please try again'
        
    test = {"job":the,"name":the}
    test = json.dumps(test, indent = 4) 
    return {
        'statusCode': 200,
        'body': test
    }

