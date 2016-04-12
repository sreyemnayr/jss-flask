# jss-flask

Currently, just a simple Python web server that sends an "Update Inventory" command

## Prerequisites
* Python 2.x with pip
* Flask
	pip install Flask
* requests
	pip install requests

## Usage:
* On your server: 
	python /path/to/jss-flask.py

## In a configuration profile:
* Create a new configuration profile
* As the payload, create a webclip with the address http://yourserver:500/update/$JSSID 
* Scope it to devices you want to have push-button update access (for me, all of them)