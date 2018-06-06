# Official Node image for fat version  
# FROM node:argon  
# Awesome tiny node image  
FROM alpine  
RUN apk update && apk upgrade  
RUN apk add nodejs tzdata  
RUN cp /usr/share/zoneinfo/Europe/Paris /etc/localtime  
  
WORKDIR /app  
ADD . /app  
RUN npm install && npm install -g forever  
EXPOSE 3000  
# launch should be done using : -e NODE_ENV=XXX  
ENTRYPOINT [ "forever", "." ]  

