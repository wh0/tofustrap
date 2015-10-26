import os

import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
	secret = os.urandom(16).encode('hex')
	response = flask.render_template('index.html')
	return response, 200, {
		# Put the page in an origin and relinquish control by forgetting its name.
		'Content-Security-Policy': 'suborigin s%s' % secret,
		# The page will be loaded again by the appcache;
		# make sure it uses the same response.
		'Cache-Control': 'public, max-age=30',
	}

port = int(os.environ.get('PORT', '5000'))
app.run(host='0.0.0.0', port=port, debug=True)
