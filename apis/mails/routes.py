from flask_restplus import Resource
from .db import *

def init_routes(api, model):
  @api.route('/')
  class ListInstances(Resource):
    @api.doc("list")
    @api.marshal_list_with(model)
    def get(self):
      '''list'''
      return listMails()
    @api.doc('find')
    @api.expect(model)
    @api.marshal_list_with(model)
    def put(self):
      '''find'''
      return findMail(api.payload)
    @api.doc('new', body=model)
    @api.expect(model)
    @api.marshal_with(model)
    def post(self):
      '''new'''
      return newMail(api.payload)
    @api.doc('bulk_delete')
    def delete(self):
      '''bulk delete'''
      return bulkDeleteMails(api.payload)

  @api.route('/<int:id>')
  class Instance(Resource):
    @api.doc('update', body=model)
    @api.expect(model)
    @api.marshal_with(model)
    def put(self, id):
      '''update'''
      return updateMail(id, api.payload)
    @api.doc('delete')
    @api.marshal_with(model)
    def delete(self, id):
      '''delete'''
      return deleteMail(id)
    pass
