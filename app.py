import adafruit_mlx90614
import board
from flask import Flask, jsonify, request
# Importing modules for the board and mlx. Uncomment in production

app = Flask(__name__)



@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

# Route for body temperature
@app.route('/body_temperature', methods=['GET'])
def body_temperature():
    i2c = board.I2C()
    mlx = adafruit_mlx90614.MLX90614(i2c)
    #return jsonify(massage="37.1")
    return jsonify(massage=mlx.object_temperature)

# For ambient temperature
@app.route('/ambient_temperature', methods=['GET'])
def ambient_temperature():
    i2c = board.I2C()
    mlx = adafruit_mlx90614.MLX90614(i2c)
    #return jsonify(massage="37.1")
    return jsonify(massage=mlx.ambient_temperature)





if __name__ == '__main__':
    app.run()
