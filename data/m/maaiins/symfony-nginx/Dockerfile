FROM nginx:1.11-alpine  
  
MAINTAINER Lauser, Nicolai <nicolai@lauser.info>  
  
ADD upstream.conf /etc/nginx/conf.d/  
ADD symfony.conf /etc/nginx/conf.d/  
  
RUN addgroup app-cache \  
&& adduser nginx app-cache \  
&& mkdir -p /app  
  
RUN ln -sf /dev/stdout /var/log/nginx/app_access.log \  
&& ln -sf /dev/stderr /var/log/nginx/app_error.log  
  
VOLUME /var/log/nginx  
VOLUME /app  
WORKDIR /app  
  
EXPOSE 80  
CMD ["nginx", "-g", "daemon off;"]

