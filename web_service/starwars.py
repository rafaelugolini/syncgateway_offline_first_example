from random import randint

import requests

MIN_PERSON_ID = 1
MAX_PERSON_ID = 104
GATEWAY_DB = 'http://gateway:4984/db/'


class Person:

    def get_random(self):
        res = requests.get('http://swapi.co/api/people/{}'.format(
            randint(MIN_PERSON_ID, MAX_PERSON_ID)
        ))
        self.status_code = res.status_code
        self.json = res.json()

    def save(self):
        self.get_random()
        url = f'{GATEWAY_DB}{self.document_id}?rev={self.revision}'
        if self.status_code == 200:
            requests.put(
                url,
                json={
                    'name': self.json.get('name'),
                    'height': self.json.get('height'),
                    'mass': self.json.get('mass'),
                    'gender': self.json.get('gender'),
                    'action': 'person_success',
                }
            )
        else:
            requests.put(
                url,
                json={
                    'action': 'person_failure',
                    'error': self.json
                }
            )

    def set_document_info(self, payload):
        self.document = payload
        self.document_id = self.document.pop('_id')
        self.revision = self.document.pop('_rev')
