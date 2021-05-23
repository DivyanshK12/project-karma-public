import os
import random
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer as SIA

colors = {0:"#040070", 1:"#0004ff", 2:"#4c00ff", 3:"#7b00ff", 4:"#b300ff", 5:"#ff00aa", 
            6:"#ff006f", 7:"#ff003c", 8:"#ff0037", 9:"#ff0000", 10:"#ff0000"}

sia = SIA()

UPLOAD_FOLDER = os.path.join(os.getcwd(),"tempstore")
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_filename(filename):
    return filename.split(".")[-2]

def random_name_16(char):
    name = ''.join(random.SystemRandom().choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(15))
    return char+name

def getsentiment(string):
    sentiment = sia.polarity_scores(string)
    return sentiment