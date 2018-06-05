FROM mhart/alpine-node:5.12  
MAINTAINER tech@musedlab.org  
  
VOLUME /drone  
RUN apk add --no-cache zip python make g++ git openssh curl  
RUN npm cache clean  
  
# Fixes https://github.com/npm/npm/issues/9863  
RUN cd $(npm root -g)/npm \  
&& npm install fs-extra \  
&& sed -i -e s/graceful-fs/fs-extra/ -e s/fs\\.rename/fs.move/
./lib/utils/rename.js  
RUN npm install npm -g  
RUN mkdir -p ~/.ssh  
RUN ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts  
RUN mkdir -p /srv  
RUN mkdir -p /srv/builddir  
COPY ./package.json ./npm-shrinkwrap.json /srv/builddir/  
WORKDIR /srv/builddir  
RUN npm install  
RUN rm package.json npm-shrinkwrap.json  

