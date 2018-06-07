FROM nginx:latest  
  
EXPOSE 80 443  
RUN apt-get update  
RUN apt-get install -y libauthen-simple-ldap-perl fcgiwrap libcgi-fast-perl  
  
VOLUME /data  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY fcgiwrap /etc/init.d/fcgiwrap  
COPY start.sh /start.sh  
  
RUN chmod 755 /etc/init.d/fcgiwrap  
RUN chmod 755 /start.sh  
  
CMD ["/start.sh"]  

