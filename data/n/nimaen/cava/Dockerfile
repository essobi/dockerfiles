FROM ubuntu:14.04  
MAINTAINER Arnaud Bosc <bosc.arno@gmail.com>  
  
RUN apt-get update  
RUN apt-get -y -qq install python git curl  
RUN curl -sL https://deb.nodesource.com/setup | sudo bash -  
RUN apt-get -y -qq install nodejs  
RUN npm install -g grunt-cli bower nodemon  
  
COPY . /src  
WORKDIR /src  
  
RUN bower --allow-root install  
RUN npm install --silent  
RUN grunt  
  
EXPOSE 3000  
CMD ["nodemon", "dist/index.js"]  

