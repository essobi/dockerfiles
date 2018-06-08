FROM node  
MAINTAINER Adam Lusted  
  
# create directory  
RUN mkdir findme  
  
ADD . /usr/src/findme  
WORKDIR /usr/src/findme  
  
RUN npm install forever  
RUN npm install  
  
EXPOSE 80  
CMD [ "forever start server.js" ]  

