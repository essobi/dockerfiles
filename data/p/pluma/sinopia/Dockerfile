FROM node  
  
MAINTAINER Alan Plum <me@pluma.io>  
  
ENV version 1.0.1  
RUN git clone -b v$version \--depth 1 https://github.com/rlidwka/sinopia.git  
  
WORKDIR /sinopia  
  
RUN rm -rf .git  
RUN npm install --production  
RUN npm cache clean  
  
ADD config.yaml /sinopia/config.yaml  
  
CMD ["./bin/sinopia"]  
  
EXPOSE 4873  
VOLUME /sinopia/storage  

