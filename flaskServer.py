from flask import *
import getArtData as gad

artApp= Flask(__name__)

# get api_token from https://developers.artsy.net/v2/start
api_token= ("")

url= 'https://api.artsy.net/api/artworks'
headers = {
    'X-Xapp-Token': api_token
}

@artApp.route("/")
def galleryPage():
    artworks = gad.startCollect(url= url, headers= headers)
    return render_template('structure.html', artworks=artworks)

if __name__ == "__main__":
    artApp.run(debug= False)