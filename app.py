from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

#Ping
@app.route('/ping')
def ping():
    return jsonify({"message": "pong!!!"})

#Header /products
@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"products": products, "message": "Product's List!", "Position":"16"})

#GET Default Method
@app.route('/products/<string:product_name>')
def getProdutc(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0 ):
        return jsonify({"product": productsFound})
    return jsonify({"message": "Product not found"})

#POST Method
@app.route('/products', methods=['POST'])
def addProducts():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }

    products.append(new_product)
    return jsonify({"message": "PRoduct added succesfully", "products": products})

#PUT Method <Edit>
@app.route('/products/<string:product_name>', methods = ['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message": "Product Updated",
            "product": productFound[0]
        })
    return jsonify({"message": "Product not found"})

#DELETE Method
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0 ):
        products.remove(productsFound[0])
        return jsonify ({
            "message": "Product Deleted",
            "products": products
        })
    return jsonify({"message": "Product not found"})

if __name__ == '__main__':
    app.run(debug=True, port=4000)