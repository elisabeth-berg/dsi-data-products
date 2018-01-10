from flask import Flask, render_template, request, jsonify
from model import ColorDict
app = Flask(__name__)
color_dict = ColorDict()

@app.route('/')
def index():
    return render_template('colors.html')

@app.route('/solve', methods=['POST'])
def solve():
    user_data = request.json
    color = user_data['color']
    thing = _get_thing(color)
    return jsonify({'thing': thing})

def _get_thing(color):
    return color_dict.predict(color)[0]

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
