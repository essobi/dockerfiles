FROM node:4.2  
RUN mkdir -p /usr/src/app  
COPY . /usr/src/app  
WORKDIR /usr/src/app  
RUN ["npm", "install"]  
RUN ["node_modules/.bin/gulp"]  
VOLUME /usr/src/app/data  
ENTRYPOINT ["node", "build/dist/server.js"]  
EXPOSE 8080  

