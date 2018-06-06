FROM jwilder/nginx-proxy  
MAINTAINER "Sascha Marcel Schmidt" <docker@saschaschmidt.net>  
  
COPY zzz_settings.conf /etc/nginx/conf.d/zzz_settings.conf  
COPY proxy.conf /etc/nginx/proxy.conf  
  
COPY entrypoint.sh /usr/bin/entrypoint  
RUN chmod a+x /usr/bin/entrypoint  
  
VOLUME ["/etc/nginx/certs"]  
ENTRYPOINT ["/usr/bin/entrypoint"]  
CMD ["forego", "start", "-r"]  

