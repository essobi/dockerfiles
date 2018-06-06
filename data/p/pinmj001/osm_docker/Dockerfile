FROM homme/openstreetmap-tiles:latest  
  
RUN mkdir /etc/ssl/private-copy && mv /etc/ssl/private/* /etc/ssl/private-
copy/ && rm -r /etc/ssl/private && mv /etc/ssl/private-copy /etc/ssl/private
&& chmod -R 0700 /etc/ssl/private && chown -R postgres:postgres
/etc/ssl/private  

