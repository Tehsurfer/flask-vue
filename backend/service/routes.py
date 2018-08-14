from flask import jsonify
from blackfynn import Blackfynn

from service.app import app
from service.config import Config

bf = None

# NOTE: This is a temporary workaround for instantiating the Blackfynn python client.
@app.before_first_request
def connect_to_blackfynn():
    global bf
    bf = Blackfynn(
        api_token=Config.BLACKFYNN_API_TOKEN,
        api_secret=Config.BLACKFYNN_API_SECRET,
        env_override=False,
        host=Config.BLACKFYNN_API_HOST,
        concepts_api_host=Config.BLACKFYNN_CONCEPTS_API_HOST
    )


@app.route('/api/', methods=['GET'])
def home():
    return 'Blackfynn API'


@app.route('/api/dataset/<id>', methods=['GET'])
def dataset(id):
    dataset = bf.get_dataset(id)
    return 'Dataset: {}'.format(dataset.name)