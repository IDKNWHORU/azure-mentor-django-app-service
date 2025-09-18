#!/bin/bash

gunicorn --bind=0.0.0.0 --workers=4 myproject.wsgi