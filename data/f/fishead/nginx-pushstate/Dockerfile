FROM nginx:alpine  
LABEL maintainer zhchuan7@gmail.com  
  
ENV NGINX_PORT 80  
COPY ./nginx.conf.template /etc/nginx/conf.d/default.conf.template  
COPY ./docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["nginx", "-g", "daemon off;"]  

