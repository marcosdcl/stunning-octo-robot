from typing import Type
from flask import request
from flask_restful import Resource
from flask_api import status
from daos.base_dao import BaseDao


class BaseResource(Resource):
    def __init__(self, dao: BaseDao, model_type: Type) -> None:
        self.__dao = dao
        self.__model_type = model_type

    def get(self, id = None):
        if id:
            return self.__dao.read_by_id(id)
        return self.__dao.read_all()

    def post(self):
        data = request.json
        item = self.__model_type(**data)
        self.__dao.save(item)
        return item, status.HTTP_201_CREATED

    def put(self):
        data = request.json
        id_aux = data['id_']
        if id_aux is not None:
            item = self.__dao.read_by_id(id_aux)
            for key, value in data.items():
                setattr(item, key, value)
            return self.__dao.save(item)
        return None, status.HTTP_404_NOT_FOUND

    def delete(self, id):
        item = self.__dao.read_by_id(id)
        self.__dao.delete(item)
        return None, status.HTTP_204_NO_CONTENT
        