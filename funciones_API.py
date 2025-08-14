import random
import requests

#Función de imágenes de patos.

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

#Función imágenes de perros.

def get_dog_image_url():    
    url_dog = 'https://random.dog/woof.json'
    res_dog = requests.get(url_dog)
    data_dog = res_dog.json()
    return data_dog ['url']

#Función de imágenes aleatorias.

def random_image():
    img_enviada = [get_dog_image_url(),get_duck_image_url()]
    return random.choice(img_enviada)


