FROM node:4.2.3  
RUN mkdir /src  
RUN mkdir /robomongo-uploads  
VOLUME ["/robomongo-uploads"]  
EXPOSE 4000  
ADD ./src /src  
WORKDIR /src  
RUN npm install  
  
CMD node app.js  

