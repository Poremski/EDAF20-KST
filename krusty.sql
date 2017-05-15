CREATE TABLE customers
(
    id INTEGER PRIMARY KEY,
    customer TEXT UNIQUE NOT NULL,
    address TEXT NOT NULL,
    country TEXT(2) NOT NULL
);
CREATE UNIQUE INDEX customers_customer_uindex ON customers (customer);
INSERT INTO 'customers' (customer,address,country) VALUES
('Finkakor AB','Helsingborg','SE'),
('Småbröd AB','Malmö','SE'),
('Kaffebröd AB','Landskrona','SE'),
('Bjudkakor AB','Ystad','SE'),
('Kalaskakor AB','Trelleborg','SE'),
('Partykakor AB','Kristianstad','SE'),
('Gästkakor AB','Hässleholm','SE'),
('Skånekakor AB','Perstorp','SE');

CREATE TABLE units
(
    unit TEXT PRIMARY KEY NOT NULL,
    name TEXT UNIQUE NOT NULL
);
CREATE UNIQUE INDEX units_name_uindex ON units (name);
INSERT INTO 'units' (unit, name) VALUES
('kg','kilogram'),('hg','hectogram'),('dag','decagram'),
('g','gram'),('dg','decigram'),('cg','centigram'),
('mg','milligram'),('kL','kiloliter'),('hL','hectoliter'),
('daL','decaliter'),('L','liter'),('dL','deciliter'),
('cL','centiliter'),('mL','milliliter');

CREATE TABLE ingredients
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient TEXT UNIQUE NOT NULL,
    quantity INTEGER NOT NULL,
    last_delivered_quantity INTEGER NOT NULL,
    last_delivered_date DATE
);
CREATE UNIQUE INDEX ingredients_ingredient_uindex ON ingredients (ingredient);
INSERT INTO 'ingredients' (ingredient, quantity, last_delivered_quantity) VALUES
('Flour', 100000, 0),
('Butter', 100000, 0),
('Icing sugar', 100000, 0),
('Roasted, chopped nuts', 100000, 0),
('Fine-ground nuts', 100000, 0),
('Ground, roasted nuts', 100000, 0),
('Bread crumbs', 100000, 0),
('Sugar', 100000, 0),
('Egg whites', 100000, 0),
('Chocolate', 100000, 0),
('Marzipan', 100000, 0),
('Eggs', 100000, 0),
('Potato starch', 100000, 0),
('Wheat flour', 100000, 0),
('Sodium bicarbonate', 100000, 0),
('Vanilla', 100000, 0),
('Chopped almonds', 100000, 0),
('Cinnamon', 100000, 0),
('Vanilla sugar', 100000, 0);

CREATE TABLE products
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT UNIQUE NOT NULL
);
CREATE UNIQUE INDEX products_product_uindex ON products (product);
INSERT INTO 'products' (product) VALUES
('Nut ring'),('Nut cookie'),('Amneris'),
('Tango'),('Almond delight'),('Berlinger');

CREATE TABLE recipes
(
    productId INTEGER NOT NULL,
    ingredientId INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit INTEGER NOT NULL,
    CONSTRAINT recipes_products_id_fk FOREIGN KEY (productId) REFERENCES products (id),
    CONSTRAINT recipes_ingredients_id_fk FOREIGN KEY (ingredientId) REFERENCES ingredients (id),
    CONSTRAINT recipes_units_unit_fk FOREIGN KEY (unit) REFERENCES units (unit)
);
INSERT INTO 'recipes' (productId, ingredientId, quantity, unit) VALUES
('1','1','450','g'),('1','2','450','g'),('1','3','190','g'),('1','4','225','g'),
('2','5','750','g'),('2','6','625','g'),('2','7','125','g'),('2','8','375','g'),
('2','9','3.5','g'),('2','10','50','g'),('3','11','750','g'),('3','2','250','g'),
('3','12','250','g'),('3','13','25','g'),('3','14','25','g'),('4','2','200','g'),
('4','8','250','g'),('4','1','300','g'),('4','15','4','g'),('4','16','2','g'),
('5','2','400','g'),('5','8','270','g'),('5','17','279','g'),('5','1','400','g'),
('5','10','10','g'),('6','1','350','g'),('6','2','250','g'),('6','3','100','g'),
('6','12','50','g'),('6','19','5','g'),('6','10','50','g');

CREATE TABLE orders
(
    id INTEGER PRIMARY KEY NOT NULL,
    customer INTEGER NOT NULL,
    delivery_date DATE,
    created DATE,
    CONSTRAINT orders_customers_id_fk FOREIGN KEY (customer) REFERENCES customers (id)
);

INSERT INTO 'orders' (customer, delivery_date, created) VALUES
(1, null, DATE('now')),
(2, null, DATE('now')),
(3, null, DATE('now'));

CREATE TABLE product_orders
(
  id INTEGER PRIMARY KEY NOT NULL,
  product INTEGER NOT NULL,
  'order' INTEGER NOT NULL,
  quantity INTEGER NOT NULL,
  created DATE,
  CONSTRAINT pallets_products_id_fk FOREIGN KEY (product) REFERENCES products (id),
  CONSTRAINT pallets_orders_id_fk FOREIGN KEY ('order') REFERENCES orders (id)
);

INSERT INTO 'product_orders' (product, 'order', quantity, created) VALUES
(1, 1, 3, DATE('now')),
(2, 1, 1, DATE('now')),
(3, 1, 2, DATE('now')),
(2, 2, 2, DATE('now')),
(3, 2, 1, DATE('now')),
(4, 3, 2, DATE('now')),
(5, 3, 4, DATE('now')),
(6, 3, 1, DATE('now'));


CREATE TABLE pallets
(
  barcode INTEGER PRIMARY KEY NOT NULL,
  product INTEGER NOT NULL,
  'order' INTEGER NOT NULL,
  location TEXT NOT NULL,
  blocked BOOLEAN DEFAULT FALSE,
  created DATE,
  CONSTRAINT pallets_products_id_fk FOREIGN KEY (product) REFERENCES products (id),
  CONSTRAINT pallets_orders_id_fk FOREIGN KEY ('order') REFERENCES orders (id)
);