from chalice import Chalice

app = Chalice(app_name='sample-api')


@app.route('/')
def index():
    return {'hi': 'anna'}

@app.route('/anna')
def anna():
    return {'hi!': 'there!'}

