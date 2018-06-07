FROM debian:jessie  
  
RUN apt-get update && apt-get install -y lighttpd  
  
ADD lighttpd.conf /etc/lighttpd/  
  
RUN lighttpd -t -f /etc/lighttpd/lighttpd.conf  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN echo "hello"  
  
ENTRYPOINT ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]  
  

