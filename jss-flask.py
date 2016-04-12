#!/usr/local/bin/python

from flask import Flask
import requests

app = Flask(__name__)

jss_user = '#jssapiuser'
jss_pass = '#jssapipass'
jss_url = 'https://#jsshostname:8443'

@app.route("/")
def hello():
	return "JSS Inventory Update Utility"

@app.route('/update/<id>')
def update_inventory(id):
	url = jss_url+'/JSSResource/mobiledevicecommands/command/UpdateInventory/id/' + id
	r = requests.post(url, auth=(jss_user,jss_pass), verify=False)
	return "<html><body><h2>Update Inventory Command Sent for device #"+id+".</h2><pre>"+r.text+"</pre></body></html>"	

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
