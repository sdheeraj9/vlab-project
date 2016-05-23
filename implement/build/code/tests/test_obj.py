
# -*- coding: utf-8 -*-
import unittest
from unittest import TestCase
from datetime import datetime

from src.obj import *
from src.op_exceptions import AttributeRequired

class TestName1(TestCase):
    TESTING = True
    def test_name_type(self):
        print "test_name_type"
        new_name = Name("John")
        # correct name
        self.assertEqual(new_name.value, "John")
        # incorrect name
        self.assertEqual(new_name.value, "123dasd")

class TestName2(TestCase):
    TESTING = True
    def test_name_type(self):
        print "test_name_type"
        new_name = Name("John")
        self.assertEqual(new_name.value, "J@67697vjhdcs")

class TestName3(TestCase):
    TESTING = True
    def test_name_type(self):
        print "test_name_type"
        new_name = Name("John")
        self.assertEqual(new_name.value, "#$%&^   HKJ   5678")

class TestEmail1(TestCase):
    TESTING = True
    def test_email_type(self):
        print "test_name_type"
        new_email = Email("abc@gmail.com")
        # correct email
        self.assertEqual(new_email.value,"abc@gmail.com")
        # incorrect email
        self.assertEqual(new_email.value,"abc@vmnv@gmail.com")       

class TestEmail2(TestCase):
    TESTING = True
    def test_email_type(self):
        print "test_name_type"
        new_email = Email("abc@gmail.com")
        self.assertEqual(new_email.value, "qww@fnbnm")    

class TestEmail3(TestCase):
    TESTING = True
    def test_email_type(self):
        print "test_name_type"
        new_email = Email("abc@gmail.com")
        self.assertEqual(new_email.value,"abcgmail.com")
        

    def test_set_email(self):
        print"test_set_email"
        user = User(name=Name("abc"), email = Email("abc@gmail.com"),
        role=Role(name=Name("admin")))
        user.setEmail(Email("abc@gmail.com"))
        self.assertEqual(user.email, "abc@gmail.com")

    def test_set_Name(self):
        print"test_set_email"
        user = User(name=Name("abc"), email = Email("abc@gmail.com"),
        role=Role(name=Name("admin")))
        user.setName(Name("abc"))
        self.assertEqual(user.name, "abc")

    def test_set_role(self):
        print"test_set_email"
        user = User(name=Name("abc"), email = Email("abc@gmail.com"),
        role=Role(name=Name("admin")))
        user.setRole(Role(name=Name("admin")))
        self.assertEqual(user.role.name, "admin")

    def test_get_role(self):
        print"test get role"
        user = User(name=Name("abc"), email = Email("abc@gmail.com"),
        role=Role(name=Name("admin")))
        new_role = user.getRole()
        self.assertEqual(new_role.name, user.role.name)

    def test_get_email(self):
        print"test get email"
        user = User(name=Name("abc"), email = Email("abc@gmail.com"),
        role=Role(name=Name("admin")))
        new_email = user.getEmail()
        self.assertEqual(new_email, user.email)

    def test_get_name(self):
        print"test get name"
        user = User(name=Name("abc"), email = Email("abc@gmail.com"),
        role=Role(name=Name("admin")))
        new_name = user.getName()
        self.assertEqual(new_name, user.name)

    def test_user_get_all(self):
        print"test get all"
        user1 = User(name=Name("abc"), email = Email("abc@gmail.com"),
        role=Role(name=Name("admin")))
        user2 = User(name=Name("pqr"), email = Email("pqr@gmail.com"),
        role=Role(name=Name("user")))
        new_user = User.get_all()
        self.assertEqual(User.users, new_user)

class TestUser(TestCase):
    TESTING = True

    def test_user_creation_without_role(self):
        print "test_user_creation_without_email"
        with self.assertRaises(AttributeRequired):
            user=User(name=Name("abc"),email=Email("abc@gmail.com"))

    def test_user_creation_without_email(self):
        print "test_user_creation_without_role"
        with self.assertRaises(AttributeRequired):
            user=User(name=Name("abc"),role=Role(name=Name("admin")))  

    def test_user_creation_without_email_and_role(self):
        print "test_user_creation_without_role_and_email"
        with self.assertRaises(AttributeRequired):
            user=User(name=Name("abc")) 

    def test_user_creation_with_role(self):
        print "test_user_creation_with_role"
        with self.assertRaises(TypeError):
            user=User(name=Name("abc"),email=Email("abc@gmail.com"),role=Role(name=Name("admin")))

class TestRole(TestCase):
    TESTING = True
    def test_role_creation(self):
        print "test_role_creation"

    def test_role_set_name(self):
        print "test_role_set_name"

    def test_role_get_all(self):
        print "test_role_get_all"

if __name__ == '__main__':
    unittest.main()
