FROM debian:jessie  
MAINTAINER Stijn Debrouwere <stijn@debrouwere.org>  
  
# All of these packages except for the google-api-python-client support  
# Python 3, so hopefully we will get to switch at some point in the  
# near future.  
RUN apt-get update && apt-get -y upgrade && apt-get -y install python python-
pip  
RUN pip install \  
tweepy==3.2 \  
tortilla==0.4 \  
google-api-python-client==1.2 \  
facepy==1.0 \  
facebookinsights==0.3 \  
boto==2.36 \  
csvkit==0.9 \  
flask==0.10 \  
flask-httpauth==2.3 \  
gunicorn==19.2 \  
honcho==0.6 \  
mock==1.0.1 \  
mailchimp==2.0.9 \  
vinepy==0.6.3  

