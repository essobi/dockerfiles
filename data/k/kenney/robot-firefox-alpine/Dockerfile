FROM python:2-alpine  
  
MAINTAINER Kenney He <kenneyhe@gmail.com>  
  
LABEL version "1.0.0.4"  
  
LABEL description "Image of a robot test framework \  
system that is used for automating testing. see
https://hub.docker.com/r/kenney/robot-firefox-alpine/"  
#
https://books.google.com/books?id=4xQKBAAAQBAJ&pg=PA59&lpg=PA59&dq=docker+container+background+command&source=bl&ots=wv5Ibu2cCY&sig=5e37HNsf5pZB4AEdRg6Buur8n6U&hl=en&sa=X&ei=w1CQVZGsGIH9oASn35bYCQ&ved=0CDYQ6AEwAjgK#v=onepage&q=docker%20container%20background%20command&f=false  
WORKDIR /tmp  
  
RUN pip install --upgrade pip  
ADD requirements.txt /tmp  
ADD repo /etc/apk/repositories  
RUN pip install -r requirements.txt  
RUN apk update  
RUN apk add xvfb dbus fontconfig ttf-freefont firefox  

