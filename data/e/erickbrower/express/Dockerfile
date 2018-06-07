FROM erickbrower/base  
  
RUN . /opt/scripts/mongodb/v2.4/install.sh  
  
RUN npm install -g grunt-cli  
RUN npm install -g bower  
RUN npm install -g express-generator  
  
RUN mkdir /opt/app  
WORKDIR /opt/app  
  
ONBUILD ADD ./package.json /tmp/package.json  
ONBUILD RUN cd /tmp && npm install  
ONBUILD ADD . /opt/app  
ONBUILD RUN rm -rf /opt/app/node_modules && cp -a /tmp/node_modules /opt/app/  

