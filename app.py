from flask import Flask, redirect
from routes.taxi_routes import taxi_bp
from routes.driver_routes import driver_bp
from routes.dashboard_routes import dashboard_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'This_is_not_my_secret_key'

app.register_blueprint(taxi_bp, url_prefix='/')
app.register_blueprint(driver_bp, url_prefix='/')
app.register_blueprint(dashboard_bp, url_prefix='/')

@app.route('/')
def home():
    return redirect('/dashboard')

if __name__ == '__main__':
    app.run(debug=True)
