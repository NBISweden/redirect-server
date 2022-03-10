import os
from flask import Flask,redirect,request

app = Flask(__name__)

@app.route('/')
def redirect_handler():
    
    # define redirects
    redirect_urls = {
               'dropin.meet.nbis.se':'https://uu-se.zoom.us/j/65398963465', 
               }

    # redirect to the correct url, print error if redirect not found
    try:
        return redirect(redirect_urls[request.headers['host']], code=302)
    except KeyError:
        return "Invalid redirection url."


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
