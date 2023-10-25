from datetime import datetime
from . import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    stock_entries = db.relationship('StockEntry', backref='product', lazy=True)
    sales = db.relationship('Sales', backref='product', lazy=True)


class StockEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    document_id = db.Column(db.String(50), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    cost_price = db.Column(db.Float, nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False)

class SalesEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    document_id = db.Column(db.String(50), unique=True, nullable=False)
    sold_quantity = db.Column(db.Integer, nullable=False)
    sale_price = db.Column(db.Float, nullable=False)
    sales_details = db.relationship('SalesDetail', backref='sales', lazy=True)
    margin = db.relationship('Margin', backref='sales', lazy=True, uselist=False)  # One-to-One relationship
    transaction_date = db.Column(db.DateTime, nullable=False)


class SalesDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sale_id = db.Column(db.Integer, db.ForeignKey('SalesEntry.id'), nullable=False)
    stock_entry_id = db.Column(db.Integer, db.ForeignKey('StockEntry.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    sale_price = db.Column(db.Float, nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False)


