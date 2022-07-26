from flask import Flask, jsonify, request

#Flast 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌
app = Flask(__name__)

#자원
menus = [
    {'id':1,'name':'Espress','price':3800},
    {'id':2,'name':'Americano','price':3500},
    {'id':3,'name':'CafeLatte','price':4100}
]

@app.route('/')
def hello_flask():
    return 'Hello World!'
    
# GET /menus | 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    return jsonify({"menus" : menus})

# POST /menus | 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
#전달받은 자료를 menus 자원에 추가
def create_menu(): #request가 JSON이라고 가정
    request_data = request.get_json() # {'name':..., 'price':...}
    id = len(menus)+1 #메뉴 id 증가
    new_menu = {
        'id' : id,
        'name' : request_data['name'],
        'price' : request_data['price']
        }
    menus.append(new_menu)
    return jsonify(new_menu)

#PUT /menus | update
@app.route('/menus/<int:id>', methods = ['PUT'])
def update_menu(id):
	request_data = request.get_json()

	update_menu = {
		'id' : id,
		'name' : request_data['name'],
		'price' : request_data['price']
	}
	menus[id-1] = update_menu
	return jsonify(update_menu)

@app.route('/menus/<int:id>', methods = ['DELETE'])
def delete_menu(id):
	del menus[id-1]
	return{
		'delete' : 'success'
	}
	
    
if __name__ == '__main__':
    app.run()