from flask import Flask,send_file, make_response, request,jsonify

app = Flask(__name__, static_url_path='')



@app.route('/pressed')
def pressed():
    direct = request.args.get('dir')
    side = request.args.get('side')
    print(direct)
    print(side)

    #here is where I send info to the GPIO pins
    #if side == 'left':
    #   if dir == 'up':
    #       leftMotor.forward()
    #   else:
    #       leftMotor.reverse()
    #elif side == 'right':
    #   if dir == 'up':
    #       rightMotor.forward()
    #   else:
    #       rightMotor.reverse()
    return 'pressed'

@app.route('/released')
def released():
    direct = request.args.get('dir')
    side = request.args.get('side')
    print(direct)
    print(side)

    #here is where I send info to the GPIO pins
    #if side == 'left':
    #   if dir == 'up':
    #       leftMotor.stop()
    #   else:
    #       leftMotor.stop()
    #elif side == 'right':
    #   if dir == 'up':
    #       rightMotor.stop()
    #   else:
    #       rightMotor.stop()
    return 'pressed'


@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    #leftMotor.stop()
    #rightMotor.stop()
	app.run()
