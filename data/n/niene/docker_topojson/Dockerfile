# Operating system image:  
FROM node:latest  
MAINTAINER Niene Boeijen <niene@webmapper.net>  
  
ENV DATA_DIR data_in  
RUN mkdir -p $DATA_DIR  
RUN apt-get -qq update && apt-get -qq --yes upgrade \  
&& npm install -g topojson  
  
  

