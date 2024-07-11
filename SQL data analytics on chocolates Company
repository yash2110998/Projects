select * from sales;
select * from geo;
select * from people;
select * from products;

select count(*) from sales;
select count(Amount) from sales;
select count(*)from people;
select count(*) from people;
select count(*) from geo;

select avg(Amount) from sales;
select avg(Customers) from sales;
select avg(Boxes) from sales;
select avg(Cost_per_box) from products;

select max(Amount) from sales;
select max(Customers) from sales;
select max(Boxes) from sales;
select max(Cost_per_box) from products;

select min(Amount) from sales;
select min(Customers) from sales;
select min(Boxes) from sales;

select stddev(Amount) from sales;
select stddev(Customers) from sales;


select * from people where Team = ' ';
select * from people where Team is NULL;

SELECT *
FROM people
WHERE team IS NOT NULL AND team != '';


describe people;
describe sales;
describe geo;
describe products;

SELECT sales.Amount, geo.Geo, geo.Region
FROM sales
INNER JOIN geo
ON sales.GeoID = geo.geoID;

select sales.Amount, sales.Boxes, people.Location, people.Team
from sales
inner join people
on sales.SPID = people.SPID;

select sales.Amount, sales.Boxes, sales.Customers, sales.SaleDate, people.Location, people.Salesperson, people.Team, geo.Geo, geo.Region, products.Category, products.Cost_per_box
from sales
inner join people
on sales.SPID = people.SPID
inner join geo
on sales.GeoID = geo.GeoID
inner join products
on sales.PID = products.PID;

select GeoID, avg(Amount) as avg_amount
from sales
group by GeoID;

select GeoID, avg(Boxes) as avg_boxes
from sales
group by GeoID;

select GeoID, max(Amount) as max_amount
from sales
group by GeoID;

select GeoID, max(Boxes) as max_boxes
from sales
group by GeoID;

select GeoID, max(Customers) as max_customers
from sales
group by GeoID;


select GeoID, avg(Customers) as avg_customers
from sales
group by GeoID;

select sales.*
from sales
join geo on geo.GeoID = sales.GeoID
where geo.Geo = 'Canada';

select * from sales where GeoID = 'G3' and Amount > 5000;

select * from people
where Salesperson like 'b%';

select * from people
where Salesperson like 'a%';

select * from people
where Salesperson like '%n';

select * from people
where Salesperson like '%or%';

select * from people
where Salesperson like '_r%';

select * from people
where Salesperson like 'a___%';

select * from people
where Salesperson like 'a%n';

select * from people
where Salesperson not like 'a';

select * from Sales
where GeoID IN ('G3', 'G2');

CREATE TABLE sales_geo AS
SELECT sales.Amount, sales.Boxes, sales.SaleDate, sales.Customers
FROM sales
JOIN geo ON sales.GeoID = geo.GeoID;

CREATE TABLE sales_people AS
SELECT sales.Amount, sales.Boxes, sales.SaleDate, sales.Customers
FROM sales
JOIN people ON sales.SPID = people.SPID;

CREATE TABLE sales_products AS
SELECT sales.Amount, sales.Boxes, sales.SaleDate, sales.Customers
FROM sales
JOIN products ON sales.PID = products.PID;

show tables;

select * from sales_people;


CREATE TABLE sales_products1 AS
SELECT sales.Amount, sales.Boxes, sales.SaleDate, sales.Customers
FROM sales
INNER JOIN products ON sales.PID = products.PID;
select * from sales_products1;

drop table sales_products1;

select sales.Amount, sales.Boxes, sales.GeoID, sales.SPID, geo.Geo, geo.Region, people.Team, people.Location
from((sales
inner join geo on sales.GeoID = geo.GeoID)
inner join people on sales.SPID = people.SPID);

CREATE TABLE sales_geo_peo AS
select sales.Amount, sales.Boxes, sales.GeoID, sales.SPID, geo.Geo, geo.Region, people.Team, people.Location
from((sales
inner join geo on sales.GeoID = geo.GeoID)
inner join people on sales.SPID = people.SPID);

select * from sales_geo_peo;

drop table sales_geo;
drop table sales_people;
drop table sales_products;

select sales.Amount , sales.Boxes, geo.Geo
from sales
left join geo on sales.GeoID = geo.GeoID
order by Geo;

select *
from sales
cross join geo;

select *
from sales
cross join people;

select *
from sales
cross join products;




