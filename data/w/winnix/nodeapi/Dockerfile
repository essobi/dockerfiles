FROM alpine:latest  
  
# Install npm and nodejs  
RUN apk add --update nodejs  
  
# Install app dependencies  
COPY package.json /var/www/app/current/package.json  
RUN cd /var/www/app/current; npm install  
  
# Bundle app source  
COPY . /var/www/app/current  
  
EXPOSE 8080  
CMD [ "node", "/var/www/app/current/app.js" ]

