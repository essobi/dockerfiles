FROM nginx  
  
ENV CONFD_VER=0.12.0-alpha3  
  
ADD
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VER}/confd-${CONFD_VER}-linux-
amd64 /usr/local/bin/confd  
ADD scripts/start_confd_nginx /usr/local/bin/start_confd_nginx  
ADD confd /etc/confd  
RUN chmod +x /usr/local/bin/confd /usr/local/bin/start_confd_nginx  
  
CMD ["start_confd_nginx"]  

