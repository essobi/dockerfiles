FROM tommylau/nginx  
  
COPY entrypoint /usr/local/bin/entrypoint  
RUN chmod +rx /usr/local/bin/entrypoint  
  
# copy over the site configuration file  
COPY conf.d/* /etc/nginx/conf.d  
  
ENTRYPOINT ["entrypoint"]  

