FROM mhart/alpine-node  
MAINTAINER Jan Blaha  
EXPOSE 1500  
RUN apk add --update curl  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
RUN npm install --production  
  
COPY . /usr/src/app  
  
EXPOSE 1500  
HEALTHCHECK CMD curl --fail http://localhost:1500 || exit 1  
  
CMD [ "node", "index.js" ]

