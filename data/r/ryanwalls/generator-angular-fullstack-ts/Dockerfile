FROM node:0.12  
# Install global tools  
RUN npm install -g grunt-cli  
RUN npm install -g bower  
RUN npm install -g tsd  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD COPY package.json /usr/src/app/  
ONBUILD RUN npm install --unsafe-perm  
ONBUILD COPY . /usr/src/app  
ONBUILD RUN bower install --allow-root  
ONBUILD RUN tsd reinstall --save  
  
EXPOSE 9000  
CMD [ "grunt", "serve:dist" ]  

