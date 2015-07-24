import sys
from sqlalchemy import Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine('sqlite:///Survey.db')

class Response(Base):
	__tablename__ = 'response'
	q1 = Column(String(25))
	q2 = Column(String(25))
	q3 = Column(String(25))
	q4 = Column(String(25))
	q5 = Column(String(25))
	comments = Column(String(250))
	id = Column(Integer,primary_key = True)

	@property
	def serialize(self):
	# for jsonlike return
		return {
			'id': self.id,			
			'Question1': self.q1,
			'Question2': self.q2,
			'Question3': self.q3,
			'Question4': self.q4,
			'Question5': self.q5,
			'comments': self.comments,
		}
Base.metadata.create_all(engine)
