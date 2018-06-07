FROM python:3.5-alpine  
MAINTAINER Shawn McElroy <shawn@skift.io>  
  
RUN pip3 install -U pip  
RUN apk update && apk add -u supervisor  
  
# add basic supervisor config  
COPY supervisord.conf /etc/supervisord.conf  
  
CMD ["supervisord", "-n"]  

