# bicsubi_core API

## Requests
- `GET /whoami`
- github id를 반환
- Example:
{  
      "name": "cyan0212"  
}
GET /echo?string="string"

Query String : string
string 을 반환합니다.
{
   "value" : "string"
}
GET /weapon

현재 존재하는 weapon을 json 형식으로 반환합니다.
Example
[
    {
         "id": 1,
        "name": "Arrow",
        "stock": 2
    },
    {
        "id": 2,
        "name": "Lance",
        "stock": 3
    },
    {
        "id": 3,
        "name": "Sword",
        "stock": 2
    }
]
POST /weapon

새로운 weapon 을 추가
BODY raw
{
    "name": "Spear",
    "stock": 1
}
새로 추가된 wapon을 json형식으로 반환합니다.
{
    "id": 4,
    "name": "Spear",
    "stock": 1
}
DELETE /weapon

현재 존재하는 특정 weapon 을 삭제합니다.
삭제된 weapon을 json형식으로 반환합니다.
Example
{
    "id": 3,
    "name": "Sword",
    "stock": 2
}
PUT /weapon

현재 존재하는 weapon 에서 특정 속성(이름, 수량)을 변경합니다.
BODY raw
{
    "name": "Lance",
    "stock": 3
}
변경된 weapon을 json형식으로 반환합니다.
[
    {
        "id": 2,
        "name": "Lance",
        "stock": 3
    }
]