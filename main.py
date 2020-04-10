from flask import Flask, request, render_template
import sys
port = 12345
if len(sys.argv) > 1:
    port = int(sys.argv[1])

app = Flask(__name__)

@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        print('here')
        print(f)
        f.save(f.filename)
        return 'ok'


@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    print('curl -F "file=@test.jpg" http://x:%d/upload/' % port)
    app.run(host='0.0.0.0', port=port)
