FROM node:7.5  
COPY ./package.json /app/package.json  
WORKDIR /app/  
RUN npm install --loglevel warn -g grunt > /dev/null  
RUN npm install --loglevel warn > /dev/null  
  
COPY ./grunt-watcher.sh /app/grunt-watcher.sh  
COPY ./Gruntfile.js /app/Gruntfile.js  
COPY ./.eslintignore /app/.eslintignore  
COPY ./.eslintrc.js /app/.eslintrc.js  
RUN chmod a+x /app/grunt-watcher.sh  
  
RUN mkdir -p /app/web/cache && mkdir -p /app/engine/Shopware/Plugins/ && mkdir
-p /app/themes/Frontend/  
  
CMD "/app/grunt-watcher.sh"  

