FROM ubuntu  
  
RUN apt-get update  
RUN apt-get install -y haproxy vim  
RUN rm -rf /var/lib/apt/lists/*  
  
COPY confd /usr/bin/confd  
COPY etcdctl /usr/bin/etcdctl  
RUN chmod +x /usr/bin/confd  
  
RUN mkdir -p /etc/haproxy  
RUN mkdir -p /etc/confd/conf.d  
RUN mkdir -p /etc/confd/templates  
COPY haproxy.cfg.tmpl /etc/confd/templates/haproxy.cfg.tmpl  
COPY haproxy.cfg.toml /etc/confd/conf.d/haproxy.cfg.toml  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
EXPOSE 3306 22002  
CMD ["/entrypoint.sh"]  

