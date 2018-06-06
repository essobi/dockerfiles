FROM nginx:1.11.1  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
COPY entrypoint.sh /entrypoint.sh  
  
EXPOSE 80  
EXPOSE 443  
CMD ["/entrypoint.sh"]  

