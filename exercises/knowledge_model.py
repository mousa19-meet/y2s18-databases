from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = "Knowledge"
	id_table = Column(Integer, primary_key=True)
	article = Column(String)
	topic = Column(String)
	rating = Column(Integer)
	
	def __repr__(self):
		if self.rating < 7:
			return ("if you want to learn about: {}\n"
				"you should look at this wiki article called: {} \n"
				"We gave this article a rating of: {} \n"
				"Unfortunately, this article does not have a better rating. Maybe, this is an article that should be replaced soon!"
				).format(
					self.topic, self.article, self.rating)
		else:
			return ("if you want to learn about : {}\n"
				"you should look at this wiki article called : {} \n"
				"We gave this article a rating of : {} \n"
				).format(
					self.topic, self.article, self.rating,)

var1 = Knowledge(article= "rainbow",topic="weather" ,rating=6)

var2 = Knowledge(article="car and go",topic="cars",rating=10)