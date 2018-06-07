FROM python:3.5-onbuild  
# Install dockerize https://github.com/jwilder/dockerize  
ENV DOCKERIZE_VERSION v0.2.0  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
CMD ["/usr/src/app/docker-cmd-webserver.sh"]  

