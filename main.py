from models import Product, app, db
from flask import render_template, request, redirect, url_for


@app.route('/')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = float(request.form['price'])
        new_product = Product(name=name, price=price)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('products'))
    return render_template('add_product.html')





@app.route('/update_product/<int:product_id>', methods=['GET', 'POST'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.price = float(request.form['price'])
        db.session.commit()
        return redirect(url_for('products'))
    return render_template('update_product.html', product=product)


@app.route('/delete_product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('products'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)