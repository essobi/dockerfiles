FROM node:8.1.4  
MAINTAINER "HMCTS Evidence Team <https://github.com/hmcts>"  
LABEL maintainer = "HMCTS Evidence Team <https://github.com/hmcts>"  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json .  
COPY yarn.lock .  
  
RUN yarn install  
  
COPY . .  
RUN yarn setup  
  
EXPOSE 8080  
CMD [ "yarn", "start" ]  

