#Grab the latest alpine image
FROM python:3.7-stretch


RUN apt update -y && apt install vim -y
# Install python and pip
ADD ./requirements.txt /tmp/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -q -r /tmp/requirements.txt

# Add our code
ADD ./pkg /opt/twitter-rm/pkg
WORKDIR /opt/twitter-rm/pkg

ENV FLASK_APP=main.py
ENV FLASK_ENV=development
# Expose is NOT supported by Heroku
# EXPOSE 5000 		

# Run the image as a non-root user
RUN adduser runner
USER runner

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku			
CMD  flask run --host=0.0.0.0 --port=$PORT