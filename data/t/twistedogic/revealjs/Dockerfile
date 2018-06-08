FROM google/nodejs:latest  
MAINTAINER Jordan Li  
RUN apt-get update -y && apt-get install ghostscript wget -y  
WORKDIR /app  
ADD . /app  
RUN npm install  

