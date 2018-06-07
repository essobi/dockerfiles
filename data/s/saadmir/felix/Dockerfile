FROM mhart/alpine-node:8  
RUN apk update && apk upgrade && apk add --no-cache --update python make gcc
g++  
  
EXPOSE 3000  
COPY . /felix  
WORKDIR /felix  
  
RUN npm install  
#RUN npm run install-frontend  
#RUN ./node_modules/.bin/gulp build-prod  
#RUN cp -rf /zweb/dist/public /var/www/  
CMD ./node_modules/.bin/gulp serve  

