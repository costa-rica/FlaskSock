from flask import Blueprint
from flask import render_template, current_app, send_from_directory
import os
from app_package._common.utilities import custom_logger
import json

from flask_sock import Sock
import time
import threading

sock = Sock()

logger_bp_admin = custom_logger('bp_admin.log')
bp_admin = Blueprint('bp_admin', __name__)

path_to_json_current = os.path.join('/Users/nick/Documents/_project_resources/WhatSticks13/apple_service_helpers/current_jobs.json')
path_to_json_complete = os.path.join('/Users/nick/Documents/_project_resources/WhatSticks13/apple_service_helpers/completed_jobs.json')

@bp_admin.route("/admin", methods=["GET","POST"])
def admin():
    logger_bp_admin.info(f"-- in admin page route --")


    with open(path_to_json_complete) as f:
        completed_data = json.load(f)

    # data_dict = completed_data.to_dict()

    return render_template('admin/admin.html', completed_data=completed_data, data_dict=completed_data)


@bp_admin.route("/admin02", methods=["GET","POST"])
def admin02():
    logger_bp_admin.info(f"-- in admin02 page route --")


    with open(path_to_json_complete) as f:
        completed_data = json.load(f)


    return render_template('admin/admin02.html', completed_data=completed_data, data_dict=completed_data)


@sock.route('/ws')
def websocket(ws):
    # Add the WebSocket connection to the list of clients
    clients.append(ws)
    try:
        while True:
            # Wait for messages from the client
            message = ws.receive()
            if message is None:
                break
    finally:
        # Remove the WebSocket connection when disconnected
        clients.remove(ws)

clients = []

# Function to monitor the JSON file for changes every second
def monitor_json_file():
    last_content = None
    while True:
        with open(path_to_json_complete, 'r') as f:
            # print("- looping ..")
            data = json.load(f)
        
        # Check if content has changed
        if data != last_content:
            print("- send data")
            last_content = data
            for client in clients:
                client.send(json.dumps(data))  # Send updated data to all clients

        time.sleep(3)  # Check for changes every second

# Start the file monitoring in a background thread
monitor_thread = threading.Thread(target=monitor_json_file, daemon=True)
monitor_thread.start()


# Global variable to store WebSocket connections

# Associate the Sock instance with the blueprint
sock.init_app(bp_admin)

# # Website Assets static data
# @bp_main.route('/website_assets_favicon/<filename>')
# def website_assets_favicon(filename):
#     logger_bp_main.info("-- in website_assets_favicon -")
#     file_to_server = os.path.join(current_app.config.get('DIR_ASSETS_FAVICONS'), filename)
#     logger_bp_main.info(f"file_to_server: {file_to_server}")
#     return send_from_directory(current_app.config.get('DIR_ASSETS_FAVICONS'), filename)