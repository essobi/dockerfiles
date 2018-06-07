#Grab the latest alpine image  
FROM alpine:latest  
  
# Install python and pip  
RUN apk add \--no-cache --update python py-pip bash  
ADD ./requirements.txt /tmp/requirements.txt  
  
# Install dependencies  
RUN pip install --no-cache-dir -q -r /tmp/requirements.txt  
RUN mkdir -p /var/www/igames  
  
# Add local files to the image.  
# ADD ./server /var/www/igames/  
# Add kwarwp files to the image.  
ADD ./kwarwp /var/www/igames  
  
WORKDIR /var/www/igames/src/server  
  
# Expose is NOT supported by Heroku  
# EXPOSE 8000  
# Run the image as a non-root user  
RUN adduser -D myuser  
USER myuser  
  
# Run the app. CMD is required to run on Heroku  
# $PORT is set by Heroku  
CMD gunicorn --bind 0.0.0.0:$PORT wsgi  
#CMD gunicorn wsgi  
# Set-up app folder.  

