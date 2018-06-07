FROM mhart/alpine-node:6  
# https://github.com/Yelp/dumb-init  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.1.3/dumb-
init_1.1.3_amd64 /dumb-init  
  
# Dockerfile is used only for cloud deployment. Otherwise Dockerfile-dev used  
WORKDIR /var/www/  
COPY package.json package.json  
  
# dumb-init needs to be executable  
RUN chmod +x /dumb-init  
  
# install server dependencies  
RUN sh -c "npm install --production"  
  
EXPOSE 8080  
ENTRYPOINT ["/dumb-init"]  
CMD ["/var/www/node_modules/nodemon/bin/nodemon.js",
"/var/www/server/index.js"]  
  

