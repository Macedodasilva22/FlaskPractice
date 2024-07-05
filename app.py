from flask import Flask, render_template ,jsonify
from meme_flask.meme_flask import get_meme
import logging

app = Flask(__name__)

@app.route("/")
def index():
    try:
        meme_pic, subreddit = get_meme()
        return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit)
    except Exception as e:
        logging.error("Error fetching meme: %s", e)
        return "Internal Server Error", 500
    

@app.route("/get_meme")
def get_meme_route():
    try:
        meme_pic, subreddit = get_meme()
        return jsonify(meme_pic=meme_pic, subreddit=subreddit)
    except Exception as e:
        logging.error("Error fetching meme: %s", e)
        return jsonify(error="Internal Server Error"), 500

if __name__ == "__main__":
    app.run(debug=True)








#from flask import Flask, render_template
#from meme_flask.meme_flask import get_meme

#app = Flask(__name__)

#@app.route("/")
#def index():
 #   meme_pic,subreddit = get_meme()
 #   return render_template("meme_index.html", meme_pic =meme_pic, subreddit =subreddit)



#if __name__ == "__main__":
 #   app.run()