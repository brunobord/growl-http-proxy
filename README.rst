================
Growl HTTP Proxy
================

This bit of software allows you to discuss with your Growl server through a HTTP
Proxy.

If you want to convey a message that would trigger a notification, all you'll
have to do would be to send a HTTP request like this:

::

    $ curl -X POST http://127.0.0.1:5000/ -H "Content-Type: application/json" \
        -d '{"title": "My title", "message": "What an interesting message..."}'

The growl-http-proxy will pass it to your Growl server and will display a nice
notification.

Available options
=================

Only 'title' and 'message' JSON keys are mandatory.

You can see the available JSON data you can pass to the proxy, with default
values for the optional keys.

::

    {
        "title": "Notification title",
        "message": "Message...",
        "sticky": false,
        "priority": 1,
        "notification": "update"
    }

Run the server
==============

Clone this repository and install the requirements::

    pip install -r requirements.txt

Then run the proxy with the following command::

    python growl-http-proxy.py

There, you have it. Using the `curl` command you've seen on the top of this
document, you can test the server.

At the moment, it only can send notification to the '127.0.0.1' Growl daemon.

TODO
====

* Allow simple data transfer, not only JSON, for the poor guys with a
  JSON-unaware programming language.
* giving you the opportunity to send notification via your web browser, through
  the homepage.

Why that?
=========

You want to discuss with your Growl notification server. But you don't know how.
Not every language has a convenient / usable library to send messages over.

But *every* modern language has a HTTP library that can send HTTP POST requests,
along with data.

If you want to send messages from a remote client, you can use this HTTP proxy
as an interface. It'd even help you bypass filtering proxies, if you configure
this server to talk via a well-known port (80, for example).

License
=======

This source code is published under the terms of the WTFPL. According to its only
"term and condition", it states what you can or cannot do:

     0. You just DO WHAT THE FUCK YOU WANT TO.

For more details, please refer to : http://sam.zoy.org/wtfpl/
