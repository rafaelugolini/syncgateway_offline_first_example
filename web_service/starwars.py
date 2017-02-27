from random import randint

import requests

MIN_PERSON_ID = 1
MAX_PERSON_ID = 88
GATEWAY_DB = 'http://gateway:4984/db/'


class Person:

    def get_random(self):
        r = requests.get('http://swapi.co/api/people/{}'.format(
            randint(MIN_PERSON_ID, MAX_PERSON_ID)
        ))
        self.person = r.json()

    def save(self):
        self.get_random()
        requests.put(
            f'{GATEWAY_DB}{self.document_id}?rev={self.revision}',
            json={
                'name': self.person.get('name'),
                'height': self.person.get('height'),
                'mass': self.person.get('mass'),
                'gender': self.person.get('gender'),
                'action': 'person_success',
            }
        )

    def set_document_info(self, payload):
        self.document = payload
        self.document_id = self.document.pop('_id')
        self.revision = self.document.pop('_rev')
