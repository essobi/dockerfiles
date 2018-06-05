FROM nginx:alpine  
MAINTAINER Boris Mikhaylov kaguxmail@gmail.com  
  
ENV HTPASSWD_PATH /etc/nginx/htpasswd;  
ADD nginx.conf.template /etc/nginx/conf.d/default.conf.template  
ADD entrypoint.sh /opt/entrypoint.sh  
ENTRYPOINT ["/opt/entrypoint.sh"]  
CMD ["nginx", "-g", "'daemon off;'"]  

