FROM nginx:1.13  
  
# copy configuration  
COPY conf.d/default.conf /etc/nginx/conf.d  
  
# copy www files  
COPY client /var/www/trambar/client  
COPY admin /var/www/trambar/admin  
  
# copy scripts  
COPY scripts/ssl-config /usr/local/bin/  
RUN chmod 744 /usr/local/bin/ssl-config  
  
# write ssl.conf then launch nginx  
CMD ssl-config && nginx -g "daemon off;"  

