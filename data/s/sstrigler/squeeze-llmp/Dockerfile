FROM sstrigler/squeeze  
MAINTAINER Stefan Strigler <stefan@strigler.de>  
  
RUN apt-get update  
RUN apt-get install -y php5-cgi php5-mysql php5-gd php5-suhosin php5-xcache  
RUN apt-get install -y mysql-client  
RUN apt-get install -y lighttpd  
RUN rm -rf /var/lib/apt/lists/*  
  
COPY etc /etc  
EXPOSE 80  
VOLUME ["/var/www", "/var/log"]  
  
CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]  

