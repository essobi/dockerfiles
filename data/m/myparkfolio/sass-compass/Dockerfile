FROM ruby  
  
MAINTAINER aoudin@parkeon.com  
  
VOLUME /app /var/cache/sass  
  
WORKDIR /app  
  
ENTRYPOINT ["/usr/local/sbin/entrypoint.sh"]  
  
CMD ["/usr/local/bundle/bin/sass",\  
"--cache-location", "/var/cache/sass",\  
"--compass",\  
"--poll",\  
"--require", "bootstrap-sass",\  
"--watch", "/app:/app"]  
  
RUN apt-get update && apt-get install -y ruby-compass  
  
ADD entrypoint.sh /usr/local/sbin/  
  
# Single-run shortcuts  
ADD update.sh /usr/local/bin/update-sass  
ADD update.sh /usr/local/bin/update-scss  
  
RUN chmod a+rx /usr/local/sbin/entrypoint.sh /usr/local/bin/update-* &&\  
echo PATH=/usr/local/bundle/bin/sass:$PATH > /etc/environment  

