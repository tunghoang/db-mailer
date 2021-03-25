from flask_restplus.fields import Integer, Float, String, String as Text, Date, DateTime, Boolean

def create_model(api):
  model = api.model('mail', {
    'idMail': Integer,
    'application': String,
    'receipient': String,
    'subject': String,
    'content': Text,
    'sent': Boolean,
    'queueTime': DateTime,
    'sentTime': DateTime 
  },mask='*');
  return model