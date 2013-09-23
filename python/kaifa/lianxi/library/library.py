#/usr/bin/python
import MySQLdb

class Library_db():
	
	def __init__(self):
		self.conn = MySQLdb.connect()
		self.conn.Select_db('library')
		self.cursor = self.conn.cursor()

	def insert(self):
		self.cid = cid
		self.2SBN = 2SBN
		self.bookshelf = bookshelf
		self.name = name
		self.number = number
		self.autor = autor
		self.publisher = publisher
		self.price = price
		self.profile = profile
		self.cursor.execute('insert into book (cid,2SBN,bookshelf,name,number,autor,publisher,price,profile) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)' % (self.cid,self.2SBN,self.bookshelf,
		self.name,self.number,self.autor,self.publisher,self.price,self.profile))
		return True

	def delete(self):
		self.id = id
		self.cursor.execute('delete from book where id = %s' % (self.id))
		return Ture

	def update(self):
		self.id = id
		self.bookshelf = bookshelf
		self.cursor.execute('update book set bookshelf = %s where id = %s' % ((self.bookshelf,self.id)))
		return True

	def select(self):
		self.id = id
		self.cursor.execute('select id = %s from book' % (self.id))
		self.data = self.cursor.fetchmany()
		return self.data

	
