FROM node:latest  
MAINTAINER Yevgeny Shirin <yevgeny.shirin@gmail.com>  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY . /usr/src/app  
  
RUN npm install -g ember-cli  
RUN npm install -g bower  
  
RUN npm install  
RUN bower install --allow-root  
  
EXPOSE 4200  
CMD ["ember", "server"]  

