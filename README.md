# Flask Sock

![Flask and DashAndData Logo](https://venturer.dashanddata.com/website_assets_images/dd_and_flask_02-400x209.png)

## Description
This is an example of how to make a page (/admin) that is constantly monitoring for changes to a .json file stored on the server side of the machine and display those changes real time.
- Blueprints
- No database
- No import of custom modules
- This project is an offshoot from FlaskStarter03

## How it works
- run the application
- in the bp_admin/routes.py there is a path_to_json_complete variable. The file that path_to_json_complete points to will be the one that when changed it will update in the /admin page.

