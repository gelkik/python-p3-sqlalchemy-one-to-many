from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer(),primary_key=True)
    title = Column(String())
    genre = Column(String())
    platform = Column(String())
    price = Column(Integer())

    reviews = relationship('Review',backref='game')

    def __repr__(self):
        return f"{self.id}" +\
            f"{self.title}, " +\
            f"Genre: {self.genre}, "+\
            f"Platform: {self.platform}, " + \
            f"Price: {self.price}" \

class Review(Base):
    __tablename__ = 'review'

    id = Column(Integer(),primary_key=True)
    score =  Column(Integer())
    comment =  Column(String())
    game_id = Column(Integer(),ForeignKey('games.id'))

    def __repr__(self):
        return f'Review(id={self.id}, ' + \
            f'score={self.score}, ' + \
            f'game_id={self.game_id})'
