from flask import Flask, jsonify, request

app=Flask(__name__)

items=[
    {"id":1,"name":"item1", "description":"This is item1"},
    {"id":2,"name":"item2", "description":"This is item2"},
    {"id":3,"name":"item3", "description":"This is item3"}

]

@app.route('/', methods=['GET'])
def home():
    return "Welcome to my to-do list project"

## GET
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)


## Retrieve
@app.route('/items/<int:id>', methods=['GET'])
def get_item(id):
    item=next((item for item in items if item["id"]==id),None)
    if item is None:
        return jsonify({"error":"Item not found"}), 404
    return jsonify(item)

##POST: create a new task

@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"name not found"}), 400
    new_item={
        "id":items[-1]["id"]+1 if items else 1,
        "name":request.json['name'],
        "description":request.json["description"]
    }
    items.append(new_item)
    return jsonify(new_item)


##PUT: update a task

@app.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    item=next((item for item in items if item["id"]==id),None)
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"name not found"}), 400
    items['name']=request.json.get('name',items['name'])
    items['description']=request.json.get('description',items['description'])
    return jsonify(item)

##Delete: delete a task

@app.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    # global items
    item=next((item for item in items if item["id"]==id),None)
    if item==None:
        return jsonify({"error":"Item not found"})
    else:
        items.remove(item)
        return jsonify({"message":"Item deleted"})

if __name__=="__main__":
    app.run(debug=True)


