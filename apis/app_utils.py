from hashlib import sha256
from flask import jsonify
from jwt import encode, decode
import logging
import logging.config
SALT = 'fitmailer'
logging.config.fileConfig(fname='logging.ini')
def getLogger():
  return logging.getLogger('DB_MAILER')
def doHash(str):
  str1 = SALT + str
  hashObj = sha256(str1.encode('UTF-8'))
  return hashObj.hexdigest()
def doGenJWT(obj, salt):
  return encode(obj, salt)
def doParseJWT(key, salt):
  try:
    return decode(key, salt)
  except: 
    return None
def doLog(message, error = False):
  if error:
    getLogger().error("*** %s" % message)
  else:
    getLogger().info("--- %s" % message)
def doClear(dict):
  keys = [ k for k in dict ]
  for key in keys:
    del dict[key]
def matchOneOf(str, prefixes):
  for prefix in prefixes:
    if str.startswith(prefix):
      return True
  return False
