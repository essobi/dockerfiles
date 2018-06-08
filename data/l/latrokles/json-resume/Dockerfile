FROM node:alpine  
  
RUN apk add --update git  
RUN npm install -g resume-cli  
  
WORKDIR /home  
ENTRYPOINT ["resume", "export"]  

