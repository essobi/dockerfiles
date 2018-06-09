FROM ptimof/ghost  
  
MAINTAINER Bixlabs, lclavijo@bixlabs.com  
  
ENV DIR /usr/src/ghost  
WORKDIR $DIR  
  
# Add manually css resources  
ADD screen.css /usr/src/ghost/content/themes/casper/assets/css/screen.css  
ADD ghost.css /usr/src/ghost/core/built/assets/ghost.css  
ADD post.hbs /usr/src/ghost/content/themes/casper/post.hbs  
ADD config.example.js /usr/src/ghost/config.example.js  
ADD entrypoint.sh /entrypoint.sh  
  
# currently only works for development  
ENV NODE_ENV development  
  
# Port 2368 for ghost server  
EXPOSE 2368  
CMD /entrypoint.sh npm start  

