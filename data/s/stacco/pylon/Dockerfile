FROM stacco/base:latest  
  
EXPOSE 80  
EXPOSE 443  
CMD ["nginx:start"]  
  
ADD ./nginx_signing.key /tmp/nginx_signing.key  
ADD ./install-nginx.sh /tmp/install-nginx.sh  
RUN /tmp/install-nginx.sh  
  
ADD ./commands /usr/local/bin  

