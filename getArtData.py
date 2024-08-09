import requests
from artworkClass import Artwork

def startCollect(url, headers):
    web_response= requests.get(url, headers=headers)
    art_data= web_response.json()
    return getArtworkInfo(art_data)
    
def getArtworkInfo(data):
    all_artworks= data["_embedded"]["artworks"]
    artwork_list= []
    
    for artwork in all_artworks:
        raw_id= artwork["slug"].split("-")
        art_id= " ".join(raw_id)
        title= artwork["title"]
        date= artwork["date"]
        raw_image= artwork["_links"]["image"]
        image= raw_image['href'].replace("{image_version}", "large")
        additional= artwork["additional_information"]
        print(image)
        
        art_obj= Artwork(art_id, title, date, image, additional)
        artwork_list.append(art_obj)
    
    return artwork_list
