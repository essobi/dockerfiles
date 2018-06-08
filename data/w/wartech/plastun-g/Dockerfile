FROM node:latest  
WORKDIR /src  
RUN apt-get update  
RUN apt-get install -qq -y hackrf  
EXPOSE 3000  
CMD npm run-script docker  
ADD . /src  
RUN npm install  

