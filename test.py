# -*- encoding: utf-8 -*-
from apis.mail_utils import getserver, sendmail1, quitserver
server = getserver()
content = '''
<h3>Trân trọng thông báo</h3>
<p>click vào link dưới để xác nhận. <a href="http://google.com">Click here</a></p>
'''
sendmail1(server, 'tung.hoang@gmail.com', u'Thông báo quý thầy cô', content, None)
quitserver(server)
