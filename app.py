from flask import Flask, render_template, json, request
from PIL import Image, ImageDraw, ImageFont
import os
import datetime

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/classify')
def showClassify():
    return render_template('classify.html')

@app.route('/admin')
def showAdmin():
    return render_template('admin.html')

@app.route('/delete', methods=['GET'])
def delete_folders():
    os.system('rm -rf ./cnn/training_dataset/*')
    return "OK", 200

@app.route('/train', methods=['GET'])
def train_network():
    print "entrenando red"
    return "OK", 200

@app.route('/upload_images', methods=['POST'] )
def test3():
  imgs = request.files
  name = request.form['inputName']
  date_now = datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S")
  name_folder = name+"/"
  data = dict(imgs)
  datas = data['file[]']

  create_folder = "mkdir ./cnn/training_dataset/"+name_folder
  os.system(create_folder)

  n = 1
  for key in datas:
    pwd = "./cnn/training_dataset/"+name_folder+name+str(n)+".jpg"
    img = Image.open(key)
    img.save(pwd)
    n=n+1
  return "OK", 201

@app.route('/upload_image', methods=['POST'])
def new_image():
  img = Image.open(request.files['inputFile'])
  img.save("./cnn/final.jpg")
  #os.system('bash ./cnn/run_cnn.sh')
  data  = get_results_classify()
  ###############
  print_image(data, "99,99")
    
  ##############
  return "OK", 201

def print_image(pwd, prob):
  image = Image.open(pwd)
  draw = ImageDraw.Draw(image)
  font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif.ttf", 60)
  draw.text((50, 50), prob, font=font, fill="white")
  image.show()


def get_results_classify():
  file_r = "./cnn/final.jpg"
  return file_r

if __name__ == "__main__":
    app.run(port=5002)
