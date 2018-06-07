FROM ubuntu:trusty  
  
RUN apt-get update && apt-get install -y lighttpd && apt-get clean -y  
  
EXPOSE 80  
VOLUME /var/www  
  
ENTRYPOINT ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]  

