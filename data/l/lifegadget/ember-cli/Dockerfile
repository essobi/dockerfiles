FROM node:4.4.7  
MAINTAINER Ken Snyder <ken@ken.net>  
  
# install OS deps  
RUN apt-get update \  
&& apt-get install -y python-dev  
  
# install npm deps  
RUN npm install -g bower  
RUN npm install -g ember-cli@1.13.15  
  
# install watchman  
RUN git clone https://github.com/facebook/watchman.git \  
&& cd watchman \  
&& git checkout v4.5.0 \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install  
  
# configure container  
EXPOSE 4200 35729  
WORKDIR /app  
CMD ['ember', 'serve']  

