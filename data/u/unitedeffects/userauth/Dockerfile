# United Effects  
# unitedeffects.com  
# UE UserAuth Service IMAGE  
# Copyright 2017-2018  
FROM mhart/alpine-node:9  
LABEL author="Bo Motlagh borzou@theboeffect.com"  
RUN mkdir /src  
COPY . /src  
WORKDIR /src  
RUN mv /src/config_changeme.js /src/config.js  
RUN yarn  
EXPOSE 4000  
CMD ["yarn", "start"]

