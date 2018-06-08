FROM alpine:3.4  
# Bundle app source  
COPY package.json /src/  
  
# Update  
RUN apk update  
RUN apk add nodejs  
WORKDIR /src  
RUN npm install  
  
COPY flow /src/flow  
COPY webcontent /src/webcontent  
  
EXPOSE 80  
CMD [ "npm","start" ]  

