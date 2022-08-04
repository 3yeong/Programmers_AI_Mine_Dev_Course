from flask import Flask, jsonify, request
import pymysql

app = Flask(__name__)

# 데이터베이스에 연결
db = pymysql.connect(host="localhost", port=3306, user="root", password="pwd", charset="utf8")

# cursor 설정
cursor = db.cursor(pymysql.cursors.DictCursor)
cursor.execute("USE mysql;")

@app.route('/')
def hello_flask():
    return 'Hello world'

# GET /whoami | github id
@app.route('/whoami')
def get_git_id():
    return jsonify({"name":"3yeong"})

# GET /echo?string="string"
@app.route('/echo')
def echo_string():
    st = request.args.get('string')
    return jsonify({"value" : st})

# POST /weapon | 자료를 자원에 추가한다.
@app.route('/weapon', methods=['POST'])
# 전달받은 자료를 menus 자원에 추가
def create_menu():  # request가 JSON이라고 가정
    request_data = request.get_json()  # {'name':..., 'price':...}

    sql = "INSERT INTO WEAPON(name, stock) VALUES (%s, %s)"
    data = (request_data['name'], request_data['stock'])
    cursor.execute(sql, data)

    db.commit()

    new_weapon = {'name': request_data['name'], 'stock': request_data['stock']}
    return jsonify(new_weapon)

# GET /weapon | 자료를 가지고 온다.
@app.route('/weapon')
def get_menus():
    # id 값 초기화
    sql1 = "SET @count=0;"
    cursor.execute(sql1)
    sql2 = "UPDATE WEAPON SET id=@count:=@count+1;"
    cursor.execute(sql2)
    sql = "SELECT * FROM WEAPON"
    cursor.execute(sql)
    values = cursor.fetchall()
    return jsonify(values)

# PUT /weapon | update
@app.route('/weapon/<int:id>', methods=['PUT'])
def update_menu(id):
    request_data = request.get_json()

    sql1 = "UPDATE WEAPON SET name=%s, stock=%s WHERE id=%s"
    data = (request_data['name'], request_data['stock'], id)
    cursor.execute(sql1, data)

    sql2 = "SELECT * FROM WEAPON WHERE id=%s"
    cursor.execute(sql2, id)
    value = cursor.fetchall()

    db.commit()
    return jsonify(value)

@app.route('/weapon/<id>', methods=['DELETE'])
def delete_weapon(id):
    sql1 = "SELECT * FROM WEAPON WHERE id=%s"
    cursor.execute(sql1, id)
    value = cursor.fetchone()

    sql2 = "DELETE FROM WEAPON WHERE id=%s"
    cursor.execute(sql2, id)

    db.commit()

    return jsonify(value)


if __name__ == '__main__':
    app.run()