# UE-Auth Domain Service  
# Copyright 2017  
FROM mhart/alpine-node:9  
LABEL author="borzou@theboeffect.com"  
  
RUN mkdir /src  
COPY . /src  
WORKDIR /src  
  
RUN mv /src/config_changeme.js /src/config.js  
RUN yarn  
  
EXPOSE 4030  
CMD ["node", "./bin/www"]

