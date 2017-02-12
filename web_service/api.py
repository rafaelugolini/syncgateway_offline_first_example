from flask import Flask, jsonify, request
from flask.views import MethodView

from starwars import Person
from worker import make_celery


app = Flask(__name__)
app.config.from_envvar('API_SETTINGS')

print(app.config)
celery = make_celery(app)


@celery.task(name='set_person')
def set_person(payload):
    p = Person()
    p.set_document_info(payload)
    p.save()


class PersonRequest(MethodView):
    def post(self):
        print(request.json)
        set_person.delay(request.json)
        return jsonify({'task': 'running'}), 201


person_request_view = PersonRequest.as_view('person_request')
app.add_url_rule(
    '/person_request/', view_func=person_request_view, methods=['POST'],
    strict_slashes=False
)
