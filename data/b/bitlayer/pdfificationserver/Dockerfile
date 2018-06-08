# We picked node:slim because electron doesn't seem to be compatible with
alpine.  
# Like, it's probably missing some shared libraries that electron needs and  
# we couldn't figure out how to install them.  
FROM node:slim  
  
RUN apt-get update  
RUN apt-get -y install libgtkextra-dev libgconf2-dev libnss3 libasound2
libxtst-dev libxss1 xvfb  
  
ADD package.json /opt/src/  
  
WORKDIR /opt/src  
  
RUN npm install  
  
COPY *.js /opt/src/  
  
CMD mkdir -p temp && xvfb-run -a node server.js  

