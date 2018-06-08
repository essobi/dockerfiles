FROM node:6.5  
# NPM  
COPY package.json /usr/src/  
RUN cd /usr/src && npm install  
  
# BOWER  
COPY package.json /usr/src/app/  
COPY bower.json /usr/src/app/  
COPY .bowerrc /usr/src/app/  
RUN cd /usr/src/app && ../node_modules/.bin/bower --allow-root install  
  
# APP  
COPY . /usr/src/app/  
ENV PATH
/usr/src/node_modules/.bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
WORKDIR /usr/src/app/  
RUN npm run prestart  
EXPOSE 8090 35729  
CMD npm start  

