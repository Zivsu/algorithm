#coding:utf8

from db import OperSQL

class Field(object):
	pass


class ModelMetaClass(type):
	'''
		as model metaclass
	'''

	def __new__(cls, name, bases, attrs):
		if name=='Model':
			return type.__new__(cls, name, bases, attrs)
		fields = set()
		for k, v in attrs.iteritems():
			if isinstance(v, Field):
				fields.add(k)
		for key in fields:
			attrs.pop(key)
		attrs['fields'] = fields #field set
		attrs['table'] = name.lower() # table name
		return type.__new__(cls, name, bases, attrs)


class Model(dict):
	__metaclass__ = ModelMetaClass

	def __init__(self, **kws):
		super(Model, self).__init__(**kws)
		'''保存对象的字段名和对应的值
		'''
		params = {}
		for field in self.fields:
			if hasattr(self, field):
				params[field] = self[field]
		self.params = params

	def __getattr__(self, name):
		return self[name]

	def __setattr__(self, name, value):
		self[name] = value
		'''处理新建对象,后期更改属性或者增加属性插入的情况
		如：
			u = User(name='suwen', password='123456')
		   	#u.name = 'chu'
		   	u.email = 'xxx@gmail.com'
		   	u.save()
		'''
		if name in self.fields:
			self.params[name] = value

	def save(self):
		OperSQL.insert(self.table, **self.params)

	def where(self, **kws):
		return OperSQL(self, **kws)


class User(Model):

	id = Field()
	name = Field()
	password = Field()


if __name__ == '__main__':
	# u = User(name='suwen', password='123456').save()
	# u.password = 'chu'
	# u.save()
	# User().where(name='suwen').delete()
	# User().where()
	# User().where(name='suwen', password='123456').update(password='12346')
	# print User().where(name='suwen', password='123456').select_one()
	# print User().where(name='chu').select_many()
	# print User().where(name='chu').select_one()
	# User().where().order_by(('name','password'),('desc','asc'))
	# User().where().order_by(('name','password'),('desc'))
	# User().where().order_by(('name','password'),('desc','asc')).limit(10)
	# print User().where(name='chu').count()










