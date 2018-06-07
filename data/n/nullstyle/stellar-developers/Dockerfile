FROM node:8  
MAINTAINER Scott Fleckenstein <scott@stellar.org>  
  
EXPOSE 8080  
ADD dependencies /  
RUN ["chmod", "+x", "dependencies"]  
RUN /dependencies  
  
ADD install /  
RUN ["chmod", "+x", "install"]  
RUN /install  
  
ADD start /  
RUN ["chmod", "+x", "start"]  
CMD /start  

