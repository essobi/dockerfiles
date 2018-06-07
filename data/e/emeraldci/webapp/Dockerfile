FROM node:0.12.2  
MAINTAINER Frederic Branczyk <fbranczyk@gmail.com>  
  
COPY . /app  
  
RUN apt-get update && apt-get install -y ruby-compass  
RUN cd /app; npm install -g bower grunt-cli; npm install; bower install
--allow-root;  
  
WORKDIR /app  
  
EXPOSE 5000  
CMD ["grunt", "serve"]  
  

