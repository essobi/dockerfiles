#  
# Rocketgraph NodeJS server with couchDB  
#  
# Pull base image.  
FROM rocketgraph/couchdb  
  
MAINTAINER Konstantinos Christofilos <kostas.christofilos@rocketgraph.com>  
  
#Install NodeJS 0.12  
RUN curl -sL https://deb.nodesource.com/setup_0.12 | sudo bash -  
RUN apt-get -y install nodejs  
  
#Install nodemon  
RUN npm install nodemon -g  
  
#Setup supervisord  
ADD ./supervisord.conf /etc/supervisor/supervisord.conf  
ADD ./supervisor_couchdb.conf /etc/supervisor/conf.d/supervisor_couchdb.conf  
  
RUN mkdir /node_app  
  
VOLUME ["/node_app"]  
  
EXPOSE 3000  
WORKDIR "/node_app"

