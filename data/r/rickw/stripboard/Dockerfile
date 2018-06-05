FROM nginx  
  
MAINTAINER Rick Wieman <git@rickw.nl>  
  
COPY public /usr/share/nginx/html  
  
VOLUME /externaldata  
RUN ln -fs /externaldata /usr/share/nginx/html/data  

