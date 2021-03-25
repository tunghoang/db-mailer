from apis.db_utils import DbInstance
from apis.mails.db import findMail
from apis.mail_utils import getserver, sendmail1, quitserver
import time

#db = DbInstance.getInstance()
while True:
  print('Get mail')
  try:
    results = findMail({'sent': False})
    if len(results) > 0:
      server = getserver()
      for r in results:
        sendmail1(server, r.receipient, r.subject, r.content, None)
        time.sleep(3)
      quitserver(server)
  except Exception as e:
    print(e)
  time.sleep(10)
