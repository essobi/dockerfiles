FROM node:latest  
  
RUN npm install -g grunt bower  
  
#RUN mkdir -p /usr/src/app/assets/ui/default/src  
WORKDIR /usr/src/app  
  
ENV NODE_ENV=production  
  
CMD npm start  
  
COPY package.json /usr/src/app/  
COPY assets/ui/default/package.json /usr/src/app/assets/ui/default/  
COPY assets/ui/default/src/bower.json /usr/src/app/assets/ui/default/src/  
  
RUN npm install && cd assets/ui/default && npm install && cd src && bower
install --allow-root  
  
COPY . /usr/src/app  
RUN grunt prod && cd assets/ui/default && ./node_modules/browserify/bin/cmd.js
-v -e src/main.js -t partialify -o build/build.js  

