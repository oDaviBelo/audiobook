from flask import render_template,redirect,url_for,send_file
from gtts import gTTS
from audio import app
from audio.forms import Transform
import os


@app.route("/",methods=["GET","POST"])
def redirect_homepage():
     return redirect(url_for('homepage'))


@app.route("/en",methods=["GET","POST"])
def homepage():
    formtransform = Transform()
    if formtransform.validate_on_submit():
            def audio():
                language = "en"
                text = formtransform.txt.data.strip()
                speech = gTTS(text=text, lang=language, slow=False)
                path = os.path.join(app.static_folder,"../static/textToSpeech.mp3")
                speech.save(path) 
            audio()
            return redirect(url_for('download_file')) 
    return render_template('homepage.html',form=formtransform)

@app.route("/pt_br",methods=["GET","POST"])
def pt_br():
    formtransform = Transform()
    if formtransform.validate_on_submit():
            def audio():
                language = "pt"
                text = formtransform.txt.data.strip()
                speech = gTTS(text=text, lang=language, slow=False)
                path = os.path.join(app.static_folder,"../static/textToSpeech.mp3")
                speech.save(path) 
            audio()
            return redirect(url_for('download_file')) 
    return render_template('homepage.html',form=formtransform)

@app.route("/download")
def download_file():
    path = os.path.join(app.static_folder,'textToSpeech.mp3')
    return send_file(path,as_attachment=True)
 
    