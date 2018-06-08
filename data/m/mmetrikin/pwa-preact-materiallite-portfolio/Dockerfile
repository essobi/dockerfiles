FROM node:8.4.0  
# The base node image sets a very verbose log level.  
ENV NPM_CONFIG_LOGLEVEL warn  
  
# Remove the default nginx index.html  
RUN rm -rf /var/www/html/index.nginx-debian.html  
  
COPY package.json package.json  
RUN npm install  
  
# Copy the contents of the dist directory over to the nginx web root  
COPY . .  
  
# The base node image sets a very verbose log level.  
ENV NPM_CONFIG_LOGLEVEL warn  
  
RUN npm run prod:build  
  
CMD npm run prod:start  
  
EXPOSE 8080  

