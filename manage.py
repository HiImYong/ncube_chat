#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# class People:
#    def __init__(self, name=""):
#       self.name = name

#    def get_name(self):
#        print(type(self))
#        return self.name
#    def set_name(self, name):
#        self.name = name

#    @classmethod
#    def set_aaa(cls, aaa):
#        cls.aaa = aaa

#    @classmethod
#    def set_bbb(cls, bbb):
#        cls.aaa = aaa

#    aaa = ""
#    @staticmethod
#    def set_aaa(aaa):
#        People.aaa = aaa
#    @staticmethod
#    def get_aaa():
#       return People.aaa

# p = People()
# p2 =People()

# p.set_name("aaa")
# p2.set_name("bbb")

# p.set_aaa('ccc')
# p.aaa = "ddd"

# print(p.get_name())
# print(p2.get_name())

# print(p2.get_aaa())

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
