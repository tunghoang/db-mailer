from sqlalchemy import ForeignKey, Column, Integer, Float, String, Boolean, Date, DateTime, Text
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.exc import *
from ..db_utils import DbInstance
from ..app_utils import *
from werkzeug.exceptions import *
from flask import session,request,after_this_request

__db = DbInstance.getInstance()



class Mail(__db.Base):
  __tablename__ = "mail"
  idMail = Column(Integer, primary_key = True)
  application = Column(String(20))
  receipient = Column(String(512))
  subject = Column(String(255))
  content = Column(Text)
  sent = Column(Boolean)
  queueTime = Column(DateTime)
  sentTime = Column(DateTime)

  constraints = list()
  if len(constraints) > 0:
    __table_args__ = tuple(constraints)
 
  def __init__(self, dictModel):
    if ("idMail" in dictModel) and (dictModel["idMail"] != None):
      self.idMail = dictModel["idMail"]
    if ("application" in dictModel) and (dictModel["application"] != None):
      self.application = dictModel["application"]
    if ("receipient" in dictModel) and (dictModel["receipient"] != None):
      self.receipient = dictModel["receipient"]
    if ("subject" in dictModel) and (dictModel["subject"] != None):
      self.subject = dictModel["subject"]
    if ("content" in dictModel) and (dictModel["content"] != None):
      self.content = dictModel["content"]
    if ("sent" in dictModel) and (dictModel["sent"] != None):
      self.sent = dictModel["sent"]
    if ("queueTime" in dictModel) and (dictModel["queueTime"] != None):
      self.queueTime = dictModel["queueTime"]
    if ("sentTime" in dictModel) and (dictModel["sentTime"] != None):
      self.sentTime = dictModel["sentTime"]

  def __repr__(self):
    return '<Mail idMail={} application={} receipient={} subject={} content={} sent={} queueTime={} sentTime={} >'.format(self.idMail, self.application, self.receipient, self.subject, self.content, self.sent, self.queueTime, self.sentTime, )

  def json(self):
    return {
      "idMail":self.idMail,"application":self.application,"receipient":self.receipient,"subject":self.subject,"content":self.content,"sent":self.sent,"queueTime":self.queueTime,"sentTime":self.sentTime,
    }

  def update(self, dictModel):
    if ("idMail" in dictModel) and (dictModel["idMail"] != None):
      self.idMail = dictModel["idMail"]
    if ("application" in dictModel) and (dictModel["application"] != None):
      self.application = dictModel["application"]
    if ("receipient" in dictModel) and (dictModel["receipient"] != None):
      self.receipient = dictModel["receipient"]
    if ("subject" in dictModel) and (dictModel["subject"] != None):
      self.subject = dictModel["subject"]
    if ("content" in dictModel) and (dictModel["content"] != None):
      self.content = dictModel["content"]
    if ("sent" in dictModel) and (dictModel["sent"] != None):
      self.sent = dictModel["sent"]
    if ("queueTime" in dictModel) and (dictModel["queueTime"] != None):
      self.queueTime = dictModel["queueTime"]
    if ("sentTime" in dictModel) and (dictModel["sentTime"] != None):
      self.sentTime = dictModel["sentTime"]

def __recover():
  __db.newSession()

def __doList():
  result = __db.session().query(Mail).all()
  __db.session().commit()
  return result  
  
def __doNew(instance):
  __db.session().add(instance)
  __db.session().commit()
  return instance

def __doGet(id):
  instance = __db.session().query(Mail).filter(Mail.idMail == id).scalar()
  doLog("__doGet: {}".format(instance))
  __db.session().commit()
  return instance

def __doUpdate(id, model):
  instance = getMail(id)
  if instance == None:
    return {}
  instance.update(model)
  __db.session().commit()
  return instance
def __doDelete(id):
  instance = getMail(id)
  __db.session().delete(instance)
  __db.session().commit()
  return instance
def __doFind(model):
  results = __db.session().query(Mail).filter_by(**model).all()
  __db.session().commit()
  return results


def listMails():
  doLog("list DAO function")
  try:
    return __doList()
  except OperationalError as e:
    doLog(e)
    __recover()
    return __doList()
  except InterfaceError as e:
    doLog(e)
    __recover()
    return __doList()
  except SQLAlchemyError as e:
    __db.session().rollback()
    raise e

def newMail(model):
  doLog("new DAO function. model: {}".format(model))
  instance = Mail(model)
  res = False
  try:
    return __doNew(instance)
  except OperationalError as e:
    doLog(e)
    __recover()
    return __doNew(instance)
  except SQLAlchemyError as e:
    __db.session().rollback()
    raise e

def getMail(id):
  doLog("get DAO function", id)
  try:
    return __doGet(id)
  except OperationalError as e:
    doLog(e)
    __recover()
    return __doGet(id)
  except InterfaceError as e:
    doLog(e)
    __recover()
    return __doGet(id)
  except SQLAlchemyError as e:
    __db.session().rollback()
    raise e

def updateMail(id, model):
  doLog("update DAO function. Model: {}".format(model))
  try:
    return __doUpdate(id, model)
  except OperationalError as e:
    doLog(e)
    __recover()
    return __doUpdate(id, model)
  except SQLAlchemyError as e:
    __db.session().rollback()
    raise e

def deleteMail(id):
  doLog("delete DAO function", id)
  try:
    return __doDelete(id)
  except OperationalError as e:
    doLog(e)
    __recover()
    return __doDelete(id)
  except SQLAlchemyError as e:
    __db.session().rollback()
    raise e

def findMail(model):
  doLog("find DAO function %s" % model)
  try:
    return __doFind(model)
  except OperationalError as e:
    doLog(e)
    __recover()
    return __doFind(model)
  except SQLAlchemyError as e:
    __db.session().rollback()
    raise e