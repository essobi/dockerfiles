FROM abernix/spaceglue:node-4.6.2-builddeps  
MAINTAINER Jesse Rosenberger  
  
USER root  
WORKDIR /home/node  
ONBUILD WORKDIR /home/node  
COPY scripts .  
RUN chown -R node:node /home/node/  
  
RUN ["npm", "install", "--global", "node-gyp"]  
USER node  
RUN lib/install_meteor.sh  
  
ONBUILD USER root  
ONBUILD COPY ./ /home/node/app  
ONBUILD RUN ["chown", "-R", "node:node", "/home/node/app"]  
  
ONBUILD USER node  
ONBUILD RUN lib/build_app.sh  

