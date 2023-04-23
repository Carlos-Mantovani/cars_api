from flask import Flask, make_response, jsonify, request
import mysql.connector

connection = mysql.connector.connect(
		host='localhost',
		user='user',
		password='p@ssW0rd123',
		database='flask_api_cars'
)

cursor = connection.cursor()

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/cars', methods=['GET'])
def get_cars():
	if 'id' in request.args():
		id = request.args['id']
		cursor.execute(f'SELECT * FROM cars WHERE id = {id}')
		car = cursor.fetchall()
		if cursor.rowcount != 0:
			return make_response (
				jsonify(
					message='Car found',
					data=car
				)
			)
		else:
			return make_response (
				jsonify(
					message='Car not found',
				)
			), 404
	else:
		cursor.execute(f'SELECT * FROM cars')
		cars = cursor.fetchall()
		return make_response(
			jsonify(
				message='Car list',
				data=cars
			)
		)

@app.route('/cars', methods=['POST'])
def create_car():
	car = request.json
	print(car)
	cursor.execute(f'INSERT INTO cars (brand, model, year) VALUES (%s, %s, %s)', (car['brand'], car['model'], car['year']))
	connection.commit()
	return make_response(
		jsonify(
			message='Car registered with sucess',
			data=car
		)
	)

@app.route('/cars', methods=['DELETE'])
def delete_car():
	if 'id' in request.args:
		id = request.args['id']
		cursor.execute(f'DELETE FROM cars WHERE id = {id}')
		car = cursor.fetchall()
		if cursor.rowcount != 0:
			return make_response (
				jsonify(
					message='Car deleted'
				)
			)
		else:
			return make_response (
				jsonify(
					message='Car not found'
				)
			), 404
app.run()