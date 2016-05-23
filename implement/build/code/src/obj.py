
# -*- coding: utf-8 -*-
from op_exceptions import AttributeRequired
from utils import *

class Name(object):
    value = None
    def __init__(self, value):
        # value: String 
        # if the string contains any non-alphabet and non-space character,
        # raise a type error
        if is_alphabetic_string(value):
            self.value = value
        else:
            raise TypeError('%s is not a Name!' % value)

    def __str__(self):
        return self.value

class Email(object):
    value = None
    def __init__(self, value):
        if is_email(value):
            self.value=value
        else:
            raise TypeError("%s is not an Email" % value)
    def __str__(self):
        return self.value
        

class User():
    users = [] # this is a static variable, accessed by User.users
    name = None
    email = None
    role = None

    def __init__(self, **kwargs):
        if kwargs is not None:
            for key, value in kwargs.iteritems():
                if key == 'name':
                    self.setName(value)
                if key == 'email':
                    self.setEmail(value)
                if key == 'role':
                    self.setRole(value)
            User.users.append(self)

    def setEmail(self, email):
        if isinstance(email, Email):
            existing_email = filter(lambda x: x.email == email, User.users)
            if not len(existing_email):
                self.email=email
        else:
            raise TypeError("%s is not an email" % value)

    def setName(self, name):
        if isinstance(name, Name):
            self.name=name
        else:
             raise TypeError("%s is not an name" % value)

    def setRole(self, role):
        if isinstance(role, Role):
            self.role = role
        else:
            raise TypeError("%s is not an role" % value)

    def add(user, session):
        if session.user.role is not 'admin':
            raise NotAuthorizedError("only a user with admin role can add")
        else:
            existing_user = filter(lambda x: x.email == user.email, User.users)
            if not existing_user :
                User.users.append(user)
            else:
                raise ConstraintError("user already exists")

    def getRole(self):
        return self.role

    def getEmail(self):
        return self.email

    def getName(self):
        return self.name

    @staticmethod
    def get_all():
        return User.users

    def to_client(self):
        pass
        return {
            'name': self.name,
            'email': self.email,
            'role': self.role.to_client()
        }

class Role():
    name = None
    roles = []

    def __init__(self, **kwargs):
        if not 'name' in kwargs:
            raise AttributeRequired("Not of the type Role")
        self.set_name(kwargs['name'])
    
        Role.roles.append(kwargs['name'])

    def set_name(self, name):
        if(name.value == "admin" or name.value =="user"):
            self.name = name.value
        else:
            raise TypeError("%s is not an role" % name)

    def getRole(self):
        return self.name

    @staticmethod
    def get_all():
        return Role.roles
        pass

    def to_client(self):
        pass
