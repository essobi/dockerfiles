FROM alpine:3.4  
MAINTAINER Dmitriy Belyaev "dimabelyaev27@gmail.com"  
ENV NGINX_VERSION 1.13.6  
COPY install.sh /usr/src/  
COPY nginx.key /usr/src/  
  
RUN sh -x /usr/src/install.sh  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY nginx.vh.default.conf /etc/nginx/conf.d/default.conf  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

