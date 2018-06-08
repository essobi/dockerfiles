FROM linarotechnologies/freeboard  
  
RUN chown -R root:root /var/lib/nginx \  
&& chmod -R 775 /var/lib/nginx \  
&& ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr
/var/log/nginx/error.log  
  
COPY default.conf /etc/nginx/conf.d/default.conf  
COPY nginx.conf /etc/nginx/nginx.conf  
  
EXPOSE 8080  

