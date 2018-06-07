FROM node  
  
MAINTAINER fastbean-au <fastbean_au@yahoo.com.au>  
  
RUN mkdir /application  
  
COPY . /application/  
  
RUN cd /application \  
&& npm install --production  
  
WORKDIR /application  
  
CMD npm start

