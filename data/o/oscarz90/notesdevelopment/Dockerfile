FROM alpine:latest  
#Update NodeJS  
RUN apk add --update nodejs  
  
#Install app dependencies  
COPY package.json /src/package.json  
RUN cd /src; npm install  
  
#Bundle app source  
COPY . /src  
  
EXPOSE 8080/tcp  
CMD ["node", "/src/index.js"]  

