from sqlalchemy import Column, String, Integer, Boolean, Float, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(Integer, nullable=False)


class CreateBeat(Base):
    __tablename__ = 'createbeats'
    beat_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    comment = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    user_name = Column(Integer, ForeignKey('users.user_id'))

    user_fk = relationship(User, lazy='subquery')


class CreateTrack(Base):
    __tablename__ = 'creatrack'
    beat_id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(String, nullable=False)
    comment = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    user_name = Column(Integer, ForeignKey('users.user_id'))

    user_fk = relationship(User, lazy='subquery')


class CreateVoice(Base):
    __tablename__ = 'createvoice'
    voice_id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(String, nullable=False)
    comment = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    user_name = Column(Integer, ForeignKey('users.user_id'))

    user_fk = relationship(User, lazy='subquery')


class RentEquipment(Base):
    __tablename__ = 'createrent'
    rent_id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(String, nullable=False)
    comment = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    user_name = Column(Integer, ForeignKey('users.user_id'))
    title = Column(String, nullable=False)

    user_fk = relationship(User, lazy='subquery')


class VideoProduction(Base):
    __tablename__ = 'creatvideo'
    video_id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(String, nullable=False)
    comment = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    user_name = Column(Integer, ForeignKey('users.user_id'))

    user_fk = relationship(User, lazy='subquery')