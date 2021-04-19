from apis.db_utils import DbInstance
from apis.mails.db import findMail, updateMail
from apis.mail_utils import getserver, sendmail1, quitserver
import time
from datetime import datetime
import logging
import logging.config

logging.config.fileConfig(fname='db-mailer-daemon.ini')

logger = logging.getLogger('DB_MAILER_DAEMON')

__db = DbInstance.getInstance()
while True:
  try:
    mails = findMail({'sent': False})
    if len(mails) > 0:
      server = getserver()
      for mail in mails:
        logger.info("Sendmail:mailId=%s to=%s subject=%s", str(mail.idMail), mail.receipient, mail.subject )
        try:
          sendmail1(server, mail.receipient, mail.subject, mail.content, None)
          updateMail(mail.idMail, {'sentTime': str(datetime.now()), 'sent': True})
        except Exception as e:
          updateMail(mail.idMail, {'sentTime': str(datetime.now())})
        time.sleep(3)
      quitserver(server)
  except Exception as e:
    print(e)
  __db.session().commit();
  time.sleep(30)
