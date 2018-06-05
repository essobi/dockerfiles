FROM node:7.0.0  
RUN mkdir -p /www/src  
RUN mkdir /www/view  
RUN mkdir /www/static  
COPY web/package.json /www  
WORKDIR /www  
# RUN npm install --quiet --production  
RUN npm install --quiet  
COPY web/src /www/src  
COPY web/static /www/static  
COPY web/view /www/view  

