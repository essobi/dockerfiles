# Nginx as a reverse proxy  
# for docker registry  
FROM nginx  
MAINTAINER Marc Zimmermann <marc@sloppy.io  
  
RUN apt-get update -q -y && \  
apt-get install -q -y python-setuptools && \  
easy_install supervisor  
  
RUN rm /etc/nginx/conf.d/*  
COPY flask.conf /etc/nginx/conf.d/flask.conf  
COPY supervisord.conf /etc/supervisord.conf  
  
CMD supervisord -c /etc/supervisord.conf  

