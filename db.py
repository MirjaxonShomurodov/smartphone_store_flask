from tinydb import TinyDB, Query
from pprint import pprint

class SmartphoneDB:
    def __init__(self, db_path):
        self.db_path = db_path
        self.db = TinyDB(db_path,indent=4)
        self.query = Query()


    def alll(self):
        
        brands = ['Oppo', 'Vivo', 'Nokia', 'Redmi', 'Apple', 'Huawei', 'Samsung']
        get = []
        for brand in brands:
            a = self.db.table(brand).all()
            get.append(a)
        return get
    
    def brands(self):
        """Returns all brands in the database"""
        return list(self.db.tables())
    
    def get_smartphone_by_brand(self,brand):
        """Returns all products by brand"""
        table=self.db.table(brand)
        return table.all()
    
    def get_smartphone_by_name(self, name):
        """Returns a product by name"""
        # re=self.db.table(brand).search(self.query.name==name)
        brands = ['Oppo', 'Vivo', 'Nokia', 'Redmi', 'Apple', 'Huawei', 'Samsung']
        smart = []

        for brand in brands:
            name = self.db.table(brand).search(self.query.name == name)
            if name != []:
                smart.append(name)
            return smart[0][0]

    def get_smartphone_by_price(self,price):
        """Returns a product by price"""
        brands = ['Oppo', 'Vivo', 'Nokia', 'Redmi', 'Apple', 'Huawei', 'Samsung']
        semart = []
        for brand in brands:
            all = self.db.table(brand).search(self.query.price == price)
            if all!=[]:
                semart.append(all)
        return semart[0][0]
    
    def add_smartphone(self, smartphone, brand):
        """Adds a product to the database"""
        add = {
            "name": "Redmi 6 Pro",
            "company": "Mi",
            "price": 1241.3,
            "img_url": "https://images-na.ssl-images-amazon.com/images/I/81xl7IHBw-L._SL1500_.jpg",
            "RAM": "8GB",
            "memory": "32GB Storage",
            "color": "Black"
        }
        all=self.db.search(smartphone)
        return all.insert(add)
    


    def delete_smartphone(self, brand,doc_id):
        """Deletes a product from the database"""
        add = self.db.table(brand)
        add.remove(doc_ids = [doc_id])
        return "oky"




db = SmartphoneDB("db.json")
# pprint(db.brands())
# pprint(db.alll())
# pprint(db.get_smartphone_by_brand("Redmi"))
# pprint(db.get_smartphone_by_name(brand="Redmi",name="Redmi Y2"))
# pprint(db.get_smartphone_by_price(1588.3))
# print(db.add_smartphone( "1","Apple"))
# pprint(db.delete_smartphone(brand="Apple",doc_id=1))
    
