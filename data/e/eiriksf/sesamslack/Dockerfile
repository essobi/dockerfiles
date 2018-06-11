FROM node:4-slim  
MAINTAINER Eirik "eirik.sander-fjeld@bouvet.no"  
COPY ./service /service  
WORKDIR /service  
RUN npm install  
EXPOSE 5000  
CMD [ "npm", "start" ]  

