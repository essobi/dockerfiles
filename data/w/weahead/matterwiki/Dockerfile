FROM node:6.10.1-alpine  
  
LABEL maintainer "We ahead <docker@weahead.se>"  
  
WORKDIR /server  
  
COPY matterwiki/package.json /server/  
  
RUN npm install  
  
COPY matterwiki/.babelrc \  
matterwiki/db/ \  
matterwiki/ \  
matterwiki/*.js \  
matterwiki/models/ \  
matterwiki/migrations/ \  
matterwiki/client/ \  
matterwiki/api/ \  
./  
  
RUN rm config.js && npm run build  
  
EXPOSE 5000  
VOLUME db  
  
CMD [ "npm", "start" ]  

