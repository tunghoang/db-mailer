from flask_restplus import Api
api = Api(title="Mailer microservice", version="1.0")

from .mails import create_api as create_mails
api.add_namespace(create_mails())
