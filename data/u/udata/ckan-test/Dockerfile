# A CKAN testing image with an APIfied paster  
# FROM debian:jessie  
FROM ckan/ckan:latest  
  
# Install dockerize (https://github.com/jwilder/dockerize)  
USER root  
ENV DOCKERIZE_VERSION v0.6.0  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
USER ckan  
  
COPY paster_api.py /paster_api.py  
COPY serve.sh /usr/local/bin/  
COPY production.ini $CKAN_CONFIG/  
  
EXPOSE 8000  
CMD ["serve.sh"]  

