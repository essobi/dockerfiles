FROM ruby  
  
MAINTAINER yajo.sk8@gmail.com  
  
VOLUME /app /var/cache/sass  
  
ENTRYPOINT ["/usr/local/sbin/entrypoint.sh"]  
  
CMD ["/usr/local/bundle/bin/sass",\  
"--cache-location", "/var/cache/sass",\  
"--compass",\  
"--poll",\  
"--require", "bootstrap-sass",\  
"--watch", "/app:/app"]  
  
RUN gem install bootstrap-sass compass listen  
  
ADD entrypoint.sh /usr/local/sbin/  
  
# Single-run shortcuts  
ADD update.sh /usr/local/bin/update-sass  
ADD update.sh /usr/local/bin/update-scss  
  
RUN chmod a+rx /usr/local/sbin/entrypoint.sh /usr/local/bin/update-* &&\  
echo PATH=/usr/local/bundle/bin/sass:$PATH > /etc/environment  

