FROM nginx:latest  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD bin /usr/local/bin  
VOLUME ["/etc/nginx/sites-templates"]  
ENTRYPOINT ["/bin/sh", "/usr/local/bin/start.sh"]  
CMD ["nginx"]  

