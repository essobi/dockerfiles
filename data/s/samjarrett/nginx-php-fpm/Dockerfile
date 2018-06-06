FROM nginx:alpine  
  
ENV PHP_HOST=app  
  
COPY default.template /etc/nginx/conf.d/default.template  
COPY run.sh /run.sh  
  
ENTRYPOINT ["/run.sh"]  
CMD ["nginx", "-g", "daemon off;"]

