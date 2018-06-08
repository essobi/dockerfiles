# Project Freedom  
# UE Postcard Maielr Service IMAGE  
# Copyright 2017  
FROM mhart/alpine-node  
LABEL author="borzou@theboeffect.com"  
RUN apk update  
RUN apk add git  
RUN mkdir /src  
  
COPY . /src  
WORKDIR /src  
RUN mv /src/config_changeme.js /src/config.js  
RUN npm install bower -g  
RUN npm install  
RUN bower install --allow-root  
  
EXPOSE 3001  
CMD ["node", "./bin/www"]

