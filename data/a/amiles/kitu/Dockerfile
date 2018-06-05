FROM mhart/alpine-node:5.9  
# https://github.com/Yelp/dumb-init  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.0.1/dumb-
init_1.0.1_amd64 /dumb-init  
  
WORKDIR /var/www/  
COPY package.json package.json  
  
# dumb-init needs to be executable  
RUN chmod +x /dumb-init  
RUN sh -c "npm install --production"  
  
EXPOSE 8080  
ENTRYPOINT ["/dumb-init"]  
CMD ["/var/www/node_modules/nodemon/bin/nodemon.js",
"/var/www/server/index.js"]  
  

