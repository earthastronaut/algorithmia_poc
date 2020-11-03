#!python
import sys
import os
import yaml
from flask import Flask, request, jsonify


app = Flask(__name__)
# TODO: fix debug
app.config["DEBUG"] = True
config = None

ROOT_PATH = os.path.abspath(os.path.join(__file__, '../../'))
CONFIG_PATH = os.path.join(ROOT_PATH, 'app_config.yml')

# TODO: hack to modify path
sys.path.insert(0, ROOT_PATH)
from src import poc



def load_config(config_path):
    with open(config_path) as f:
        config = yaml.safe_load(f)
    config['config_path'] = config_path
    return config


@app.route("/", methods=["GET", "POST"])
def algorithmia():
    if request.method == "GET":
        return poc.apply('bwahahaha')
    elif request.method == "POST" & request.is_json:
        data = request.get_json()
        print(data)
        data['yay'] = 'you rock, rock'
        data['poc_response'] = poc.apply(data)
        return jsonify(data)


if __name__ == "__main__":
    config = load_config(CONFIG_PATH)
    app.run(host='0.0.0.0', port=5000, debug=True)
