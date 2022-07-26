from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [
	{"id" : 1, "name":"Espresso", "price":3800},
	{"id" : 2, "name":"Americano", "price":4100},	
	{"id" : 3, "name":"CafeLatte", "price":4600},		
]

@app.route('/') #home, root
def hello_flask():
	return "Hello World!"

# GET /menus | 자료를 가지고 온다
@app.route('/menus') #menus의 접근 시도
def get_menus():
	return jsonify({"menus" : menus}) #json 파일로 돌아옴

# POST /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods = ['POST']) # get이 기본적으로 되어있음, 리스트 형태로 작성가능
def create_menu():
	# 전달받은 자료를 menus 자원에 추가 (request가 json 형태로 가정)
	request_data = request.get_json() # {'name':..., 'price':...}
	new_menu = {
        'id' : 4,
        'name' : request_data['name'],
        'price' : request_data['price']
        }
    menus.append(new_menu)
    return jsonify(new_menu)

if __name__ == '__main__':
	app.run()