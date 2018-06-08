FROM node:8.2-slim  
  
LABEL maintainer="Garasilabs"  
LABEL NodeVersion="8.2"  
LABEL ForeverJSVersion="0.14.2"  
LABEL DefaultCMD="forever --spinSleepTime 10000 --minUptime 10000
--watchIgnore /opt/apps/node_modules/ --watchIgnore /opt/apps/public/ -w
bin/www"  
  
# Install forever js version 0.14.2 (because version 0.15.3 /latest cannot
detect file change over nfs)  
RUN npm install -g forever@0.14.2  
  
# Install bower just in case need bower install  
RUN npm install -g bower  
  
# Install sequelize for migrating db  
RUN npm install -g sequelize-cli  
  
# Installing node-gyp package for compiling cross-platform native node modules  
RUN npm i -g node-gyp  
  
# make working directory  
RUN mkdir /opt/apps  
WORKDIR /opt/apps  
  
# Create user app with uid 1100 for nodejs user with limited access (non root)  
RUN useradd -u 1100 -s /bin/bash -m app  
  
# Make user app has permission to global node_modules  
RUN chown app:app /usr/local/lib/node_modules -R  
RUN chown app:app /opt/apps  
  
# set default user when running container  
USER app  
  
# Add default command if no args specified when running this image  
CMD ["forever","--spinSleepTime","10000","--minUptime","10000","--
watchIgnore","/opt/apps/node_modules/","--
watchIgnore","/opt/apps/public/","-w","bin/www"]  

