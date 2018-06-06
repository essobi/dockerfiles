FROM node:4.5  
MAINTAINER Rony Dray <contact@obigroup.fr>, Jonathan Dray
<jonathan.dray@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update \  
&& apt-get install --quiet --assume-yes --no-install-recommends \  
build-essential \  
curl \  
imagemagick \  
libffi-dev \  
nano \  
python-dev \  
sqlite3 \  
sudo \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install CoffeeScript & Cozy Controller  
RUN npm install -g \  
coffee-script \  
cozy-controller \  
cozy-monitor  
  
# Create Cozy users, without home directories.  
RUN useradd -M cozy \  
&& useradd -M cozy-data-system \  
&& useradd -M cozy-home  
  
# Container entry point  
COPY docker-entrypoint.sh /usr/local/bin/  
  
# Env variables  
# These are required by cozy to locate the  
# CouchDB instance location  
ENV NODE_ENV=production \  
COUCH_HOST=couchdb \  
COUCH_PORT=5984  
# Expose port  
EXPOSE 9002 9104  
VOLUME ["/usr/local/cozy/", "/usr/local/var/log/cozy",
"/usr/local/var/cozy/data-system/indexes"]  
  
ADD init.sh /usr/local/bin/cozy-init.sh  
  
WORKDIR /usr/local/lib/node_modules/cozy-controller/build/  
  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
CMD [ "node", "server.js" ]  

