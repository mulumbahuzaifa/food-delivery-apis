from flask import Flask, request
import requests
import json
import os

app = Flask(__name__)

url = "https://api.janja.me/v0/messages/text"
url1 = "https://api.janja.me/v0/messages/sendimage"
url2 = "https://api.janja.me/v0/messages/texturl"
url3 = "https://api.janja.me/v0/messages/sendcontact"
url4 = "https://api.janja.me/v0/messages/sendlocation"
url5 = "https://api.janja.me/v0/messages/sendaudio"
url6 = "https://api.janja.me/v0/messages/sendvideo"


headers = {
  'Authorization': 'Basic Y2Vic2FkbWluOll1QDQyMjAwMjExeHJkdA==',
  'Content-Type': 'application/json'
}




@app.route("/image/chicken-main", methods=["GET", "POST"])

def image():
    payload = json.dumps({
        "to_phonenumber": os.environ.get('receiver_number'),
        "sender_id": os.environ.get('sender_number'),
        "image_url": "https://kahwa2go.com/wp-content/uploads/2021/04/Untitled-design-2021-04-23T161059.888.png",
        "caption": "Chicken Main at 34,000UGX \n 1. Pay with Mobile Money \n 2. Pay with Card"
    })
    response = requests.request("POST", url1, headers=headers, data=payload)
    # print(response.text)
    return response.text

@app.route("/image/fish-fingers", methods=["GET", "POST"])

def image1():
    payload = json.dumps({
        "to_phonenumber": os.environ.get('receiver_number'),
        "sender_id": os.environ.get('sender_number'),
        "image_url": "https://kahwa2go.com/wp-content/uploads/2021/04/Untitled-design-2021-04-23T154705.722.png",
        "caption": "Fish-Fingers 15,000UGX \n 1. Pay with Mobile Money \n 2. Pay with Card"
    })
    response = requests.request("POST", url1, headers=headers, data=payload)
    # print(response.text)
    return response.text

@app.route("/image/fish-main", methods=["GET", "POST"])

def image2():
    payload = json.dumps({
        "to_phonenumber": os.environ.get('receiver_number'),
        "sender_id": os.environ.get('sender_number'),
        "image_url": "https://kahwa2go.com/wp-content/uploads/2021/04/Untitled-design-2021-04-23T155418.064.png",
        "caption": "Fish Main at 32,000UGX \n 1. Pay with Mobile Money \n 2. Pay with Card"
    })
    response = requests.request("POST", url1, headers=headers, data=payload)
    return response.text

@app.route("/image/jollof-chicken-rice", methods=["GET", "POST"])

def image3():
    payload = json.dumps({
        "to_phonenumber": os.environ.get('receiver_number'),
        "sender_id": os.environ.get('sender_number'),
        "image_url": "https://kahwa2go.com/wp-content/uploads/2021/04/Untitled-design-2021-04-23T155541.363.png",
        "caption": "Jollof Chicken Rice at 20,000UGX \n 1. Pay with Mobile Money \n 2. Pay with Card"
    })
    response = requests.request("POST", url1, headers=headers, data=payload)
    return response.text

@app.route("/image/cappucino", methods=["GET", "POST"])

def image4():
    payload = json.dumps({
        "to_phonenumber": os.environ.get('receiver_number'),
        "sender_id": os.environ.get('sender_number'),
        "image_url": "https://kahwa2go.com/wp-content/uploads/2021/04/Untitled-design-2021-04-23T154448.183.png",
        "caption": "Cappucino at 9,500UGX \n 1. Pay with Mobile Money \n 2. Pay with Card"
    })
    response = requests.request("POST", url1, headers=headers, data=payload)
    return response.text


@app.route("/image/roadside-chicken", methods=["GET", "POST"])

def image5():
    payload = json.dumps({
        "to_phonenumber": os.environ.get('receiver_number'),
        "sender_id": os.environ.get('sender_number'),
        "image_url": "https://kahwa2go.com/wp-content/uploads/2021/04/Untitled-design-2021-04-23T161354.497.png",
        "caption": "Road-side Chicken at 32,000UGX \n 1. Pay with Mobile Money \n 2. Pay with Card"
    })
    response = requests.request("POST", url1, headers=headers, data=payload)
    return response.text

@app.route("/image/green-juice", methods=["GET", "POST"])

def image7():
    payload = json.dumps({
        "to_phonenumber": os.environ.get('receiver_number'),
        "sender_id": os.environ.get('sender_number'),
        "image_url": "https://kahwa2go.com/wp-content/uploads/2021/04/Green-Juice-1-scaled.jpg",
        "caption": "Green juice at 15,000UGX \n 1. Pay with Mobile Money \n 2. Pay with Card"
    })
    response = requests.request("POST", url1, headers=headers, data=payload)
    return response.text


@app.route("/image/oreos", methods=["GET", "POST"])

def image6():
    payload = json.dumps({
        "to_phonenumber": os.environ.get('receiver_number'),
        "sender_id": os.environ.get('sender_number'),
        "image_url": "https://kahwa2go.com/wp-content/uploads/2021/04/Untitled-design-2021-04-23T161438.077.png",
        "caption": "Oreos at 15,500UGX \n 1. Pay with Mobile Money \n 2. Pay with Card"
    })
    response = requests.request("POST", url1, headers=headers, data=payload)
    return response.text

@app.route("/image/breakfast-combo", methods=["GET", "POST"])

def image8():
    payload = json.dumps({
        "to_phonenumber": os.environ.get('receiver_number'),
        "sender_id": os.environ.get('sender_number'),
        "image_url": "https://kahwa2go.com/wp-content/uploads/2021/04/Untitled-design-2021-04-23T155620.987.png",
        "caption": "Breakfast-Combo at 25,000UGX \n 1. Pay with Mobile Money \n 2. Pay with Card"
    })
    response = requests.request("POST", url1, headers=headers, data=payload)
    return response.text


@app.route("/image/waffles", methods=["GET", "POST"])

def image9():
    payload = json.dumps({
        "to_phonenumber": os.environ.get('receiver_number'),
        "sender_id": os.environ.get('sender_number'),
        "image_url": "https://kahwa2go.com/wp-content/uploads/2021/04/Untitled-design-2021-04-23T161218.290.png",
        "caption": "Waffles at 8,000UGX \n 1. Pay with Mobile Money \n 2. Pay with Card"
    })
    response = requests.request("POST", url1, headers=headers, data=payload)
    return response.text



if __name__ == "__main__":
    app.run(debug=True)


    