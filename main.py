from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/getTwitterHandle', methods = ['POST'])
def home():
    if(request.method == 'POST'):
        data = request.json
        print("Data: ", data)
        twitter_handle = data['payload']['payment']['entity']['notes']['twitter_handle']
        print("Twitter Handle: ", twitter_handle)
    
    return twitter_handle


# driver function
if __name__ == '__main__':

	app.run(host='0.0.0.0', port = 3000,debug = True)
