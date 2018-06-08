FROM nginx:latest  
MAINTAINER fink3l <sergio.kudrin@gmail.com>  
  
COPY ./conf /etc/nginx/conf.d/  
  
RUN mkdir -p /var/log/nginx  
RUN apt-get update && apt-get install -y vim  
RUN apt-get update && apt-get install -y iputils-ping  
RUN touch /var/log/nginx/access.log && touch /var/log/nginx/error.log  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr
/var/log/nginx/error.log  
  
CMD ["nginx", "-g", "daemon off;"]  

