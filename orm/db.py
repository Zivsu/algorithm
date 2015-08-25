#coding:utf8

import mysql.connector, logging
import ConfigParser
       
class DB(object):
	conn = None

	@classmethod
	def connect(cls):
		#read db config
		cf = ConfigParser.ConfigParser()
		cf.read('config.ini')
		params = dict(cf.items('db'))

		cls.conn = mysql.connector.connect(**params)

	@classmethod
	def commit(cls):
		if not cls.conn:
			cls.connect()
		cls.conn.commit()

	@classmethod
	def cursor(cls):
		if not cls.conn:
			cls.connect()
		return cls.conn.cursor()

	@classmethod
	def execute(cls, *args):
		cursor = cls.cursor()
		cursor.execute(*args)
		return cursor

	@classmethod
	def cleanup(cls):
		if cls.conn:
			conn = cls.conn
			conn.close()
			cls.conn = None	

class OperSQL(object):
	'''
		crud(create retrieve update delete) opetation
    '''
	def __init__(self, model, **kws):
		self.model = model
		for k in kws.keys():
			if k not in self.model.fields:
				raise ValueError('this model not exists the field about {}'.format(k))

		self.where_params = kws.values()
		self.where_exp = ' where ' + ' and '.join(['{}=%s'.format(k) for k in kws.keys()]) \
						if len(kws) else ''
		# print self.where_exp
		# print self.where_params

	@classmethod
	def insert(cls, table, **kws):
		#insert into user (username, password) values (%s, %s)
		sql = 'insert into {} ({}) values ({})'.format(table, ', '.join([k for k in kws.keys()]), 
				', '.join(['%s' for _ in range(len(kws))]))
		_params = [value for value in kws.itervalues()]
		self._execute(sql, _params) 
			

	def delete(self):
		'''
		delete data from table -- delete from users where id=2
		''' 
		sql = 'delete from {} {}'.format(self.model.table, self.where_exp)
		self._execute(sql, self.where_params) 
		

    # update students set tel=default where id=5
	def update(self, **kws):
		sql = 'update {} set {} {}'.format(self.model.table, ' and '.join(['{}=%s'.format(k)
				for k in kws.keys()]), self.where_exp)
		print sql
		_params = kws.values() + self.where_params
		print _params
		self._execute(sql, _params)

	def select_one(self):
		return self._select(True)

	def select_many(self):
		return self._select()

	def limit(self, row_num, offset=None):
		self.where_exp += ' limit %s%s' %(
			'%s, ' % offset if offset is not None else '', row_num)
		print self.where_exp
		return self


	#@param rows: 排序的列的列表
	#@param orders: 一对一映射rows
	#sql:order by company desc, ordernumber asc
	def order_by(self, rows, orders):
		if len(rows) != len(orders):
			raise ValueError('the length of two sequence is not equal')

		for r in rows: 
			if r not in self.model.fields:
				raise TypeError('not exists the field')

		order_value = ('desc', 'asc')
		for o in orders:
			if o not in order_value:
				raise ValueError('order sequence word not exists')
		self.where_exp += ' order by' \
						+', '.join([' {} {}'.format(k, v) for k, v in zip(rows, orders)])
		return self

	def count(self):
		sql = 'select count(*) from %s %s;' % (self.model.table, self.where_exp)
		print sql
		(row_cnt, ) = DB.execute(sql, self.where_params)
		DB.cleanup()
		return row_cnt

		
	'''deal with crud opetation
	'''
	def _execute(self, sql, params):
		try:
			DB.execute(sql, _params) 
			DB.commit()
		finally:
			DB.cleanup()		


	def _select(self, first=False):
		# select * from table where name='suwen'
		sql = 'select * from {}{}'.format(self.model.table, self.where_exp)
		
		cursor = DB.execute(sql, self.where_params) 
		if cursor.description:
			names = [x[0] for x in cursor.description]
		if first:
			values = cursor.fetchone()
			print values
			DB.cleanup()
			if not values:
				return None
			return self._dict(names, values)

		d = [self._dict(names, x) for x in cursor.fetchall()]
		DB.cleanup()		
		return d
		
	#deal with the data about what returns from select sentence					
	def _dict(self, names=(), values=()):
		d = {}
		for k, v in zip(names, values):
			d[k] = v
		return d


if __name__ == '__main__':
	cf = ConfigParser.ConfigParser()
	cf.read('config.ini')
	print dict(cf.items('db'))
