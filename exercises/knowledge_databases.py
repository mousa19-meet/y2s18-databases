from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(article,topic,rating):

	article_object = Knowledge(
		article=article,
		topic=topic,
		rating=rating)
	session.add(article_object)
	session.commit()

def query_all_articles():
	article = session.query(
		Knowledge).all()
	return article


def query_article_by_rating(threshold):
	rating = session.query(
		Knowledge).filter_by(
		rating=rating).first()
	if rating < threshold:
		return rating
	

def query_article_by_topic(topic):
	topic = session.query(
		Knowledge).filter_by(
		topic=topic).first()
	return topic


def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(
		topic=topic).delete()
	session.commit()


def delete_all_articles():

	session.query(Knowledge).delete()
	session.commit()


def edit_article_rating(update_rating,article_title):
	article_object = session.query(
		Knowledge).filter_by(
		article=article_title).first()
	article_object.rating = update_rating
	session.commit()






