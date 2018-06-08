FROM node  
MAINTAINER McKay Software <opensource@mckaysoftware.co.nz>  
  
CMD node . | node_modules/.bin/bunyan -Lo short  
EXPOSE 1337  
WORKDIR /parse  
  
RUN mkdir -p cloud && touch cloud/main.js  
VOLUME /parse/cloud  
VOLUME /parse/logs  
  
ENV APP_ID required  
ENV CLIENT_KEY required  
ENV CLOUD /parse/cloud/main.js  
ENV DATABASE_URI mongodb://mongo  
ENV MASTER_KEY required  
ENV PORT 1337  
ENV SERVER_URL required  
  
ADD package.json /parse/  
RUN npm install  
ADD index.js /parse/  

