
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "id" : self._generateId(),
                "first_name": "john",
                "last_name": self.last_name,
                "age": 33,
                "lucky_number" : [9,1,55],
            },
            {
                "id" : self._generateId(),
                "first_name": "jackson",
                "last_name": self.last_name,
                "age": 35,
                "lucky_number" : [23,11,4],
            },
            {
                "id" : self._generateId(),
                "first_name": "jimmy",
                "last_name": self.last_name,
                "age": 5,
                "lucky_number" : 1,

            }
        ]

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        try:
            member.update({
                    "id" : member.get("id", self._generateId())
            })
            self._members.append(member)
            return True
            
        except Exception as error:
            False
            

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True
        return False

    def get_member(self, id):
        for member in self._members:
            if id == member["id"]:
                return member
        return None
        

    def get_all_members(self):
        return self._members  #Esto se retorna para mi endpoint como un helper
