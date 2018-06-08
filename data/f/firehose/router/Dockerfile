FROM nginx  
  
ADD
https://github.com/kelseyhightower/confd/releases/download/v0.4.0/confd-0.4.0-linux-
amd64 /usr/local/bin/confd  
ADD scripts/start_confd_nginx /usr/local/bin/start_confd_nginx  
ADD confd /etc/confd  
RUN chmod +x /usr/local/bin/confd /usr/local/bin/start_confd_nginx  
  
CMD ["start_confd_nginx"]  

