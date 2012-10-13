from flask import Flask, request, abort, render_template
import Growl
import os
app = Flask(__name__)


APP_NAME = 'growl-http-proxy'
NOTIFICATIONS = ['update']
DEFAULT_ICON_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'icon.png')


def send_notification(title, message, sticky, icon, notification, priority):
    notifier = Growl.GrowlNotifier(APP_NAME, NOTIFICATIONS, applicationIcon=icon)
    notifier.register()
    notifier.notify(notification, title, message, sticky=sticky, priority=priority)


@app.route('/', methods=['POST'])
def send():
    data = request.json or request.form or {}

    if 'title' not in data or 'message' not in data:
        abort(400)  # Bad request

    sticky = data.get('sticky') or False
    icon_path = DEFAULT_ICON_PATH
    icon = Growl.Image.imageFromPath(icon_path)
    notification = data.get('notification') or 'update'
    priority = int(data.get('priority')) or 1
    send_notification(data.get('title'), data.get('message'),
        sticky, icon, notification, priority)
    return 'Message sent\n'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
