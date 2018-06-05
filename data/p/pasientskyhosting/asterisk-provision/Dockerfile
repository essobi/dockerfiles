FROM pasientskyhosting/nginx-nodejs  
MAINTAINER Andreas Krüger  
  
ENV NODE_ENV production  
ENV NODE_DEBUG false  
  
ENV TZ=Europe/Oslo  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
COPY /server.js /var/www/html/server.js  
COPY /reset.js /var/www/html/src/reset.js  
COPY /package.json /var/www/html/package.json  
  
COPY /src /var/www/html/src  
  
WORKDIR /var/www/html  
RUN npm install  
  
CMD ["node", "server.js"]  

