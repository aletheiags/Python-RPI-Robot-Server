from flask import Flask,send_file, make_response, request,jsonify
from gpiozero import Motor

#Need a config file for this part
motors = {
    'left':Motor(forward=17, backward=27),
    'right':Motor(forward=23, backward=22)
}

app = Flask(__name__, static_url_path='')

@app.route('/pressed')
def pressed():
    direct = request.args.get('dir')
    side = request.args.get('side')
    print(direct)
    print(side)

    if direct == 'up':
        motors[side].forward()
    elif direct == 'down':
        motors[side].backward()



@app.route('/released')
def released():
    direct = request.args.get('dir')
    side = request.args.get('side')
    print(direct)
    print(side)

    motors[side].stop()
    return 'released'


@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    #leftMotor.stop()
    #rightMotor.stop()
	#app.run()
    app.run(host='0.0.0.0')
