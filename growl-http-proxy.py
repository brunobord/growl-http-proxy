from flask import Flask, request
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
    sticky = request.json.get('sticky') or False
    icon_path = DEFAULT_ICON_PATH
    icon = Growl.Image.imageFromPath(icon_path)
    notification = request.json.get('notification') or 'update'
    priority = request.json.get('priority') or 1
    send_notification(request.json.get('title'), request.json.get('message'),
        sticky, icon, notification, priority)
    return 'Message sent\n'


@app.route('/', methods=['GET'])
def index():
    return "Wrong method. Request must be use the 'POST' method\n"

if __name__ == '__main__':
    app.run()
