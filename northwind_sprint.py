#!/usr/bin/env python

import sqlite3
CONN = sqlite3.connect('northwind_small.sqlite3')


def queries():

    expensive = 'SELECT * FROM Product ORDER BY UnitPrice DESC LIMIT 10;'

    avg_age = 'SELECT AVG(HireDate - BirthDate) FROM Employee;'

    city_age = ('SELECT City, AVG(HireDate - BirthDate) FROM Employee '
                   'GROUP BY City;')

    item_supply = ('SELECT p.ProductName, p.UnitPrice, s.CompanyName '
                      'FROM Product p, Supplier s WHERE p.SupplierId = s.Id '
                      'ORDER BY p.UnitPrice DESC LIMIT 10;')

    largest_category = ('SELECT c.CategoryName, COUNT(DISTINCT p.Id) '
                        'FROM Category c, Product p WHERE c.Id = p.CategoryId '
                        'GROUP BY 1 ORDER BY 2 DESC LIMIT 1;')

    employee = ('SELECT e.Id, e.FirstName, e.LastName, COUNT(DISTINCT t.Id) '
                'FROM Territory t, Employee e, EmployeeTerritory et '
                'WHERE e.Id = et.EmployeeId AND t.id = et.TerritoryId '
                'GROUP BY 1, 2, 3 ORDER BY 4 DESC LIMIT 1;')


    query = (expensive, avg_age, city_age, item_supply,
               largest_category, employee)
    curs = CONN.cursor()
    for i in query:
        print(curs.execute(i).fetchall())


if __name__ == "__main__":
    queries()


'''A document store like MongoDB is appropriate when scalability is important ie. when storing huge amount of databases. 
MongoDb is not approriate for soring smaller data like password, bookmarks etc'''

'''NewSQL is a class of relational database management system with a focus on having the scalability of NoSQL whilst 
at the same time maintaining the ACID guarantee of traditional database system. '''