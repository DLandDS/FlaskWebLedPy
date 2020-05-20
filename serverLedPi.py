import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
ledRed = 2
GPIO.setup(ledRed, GPIO.OUT)
GPIO.output(ledRed, GPIO.LOW)
ledRedSts = GPIO.input(ledRed)

templateData = {
		'ledRed' : ledRed,
    }

def update():
	ledRedSts = GPIO.input(ledRed)
	templateData['ledRed'] = ledRedSts
	print(templateData);
	return render_template('index.html', **templateData)

@app.route("/")
def index():
	return update()

@app.route("/LedControl/<action>")
def action(action):
	if action == 'on':
		GPIO.output(ledRed, GPIO.HIGH)
	if action == 'off':
		GPIO.output(ledRed, GPIO.LOW)
	
	return update()
		
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)

