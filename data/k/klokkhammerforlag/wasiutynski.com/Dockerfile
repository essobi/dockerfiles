FROM node:5.1  
EXPOSE 80  
ENV NODE_ENV production  
CMD harp server /var/www --port 80  
ENV DOCKER_CACHE_INVALIDATED 2016-02-27  
RUN npm install -g harp  
WORKDIR /var/www  
COPY . /var/www  

