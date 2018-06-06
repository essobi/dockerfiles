FROM bradjonesllc/docker-haproxy-letsencrypt:latest  
  
COPY bootstrap-pre.sh /  
  
RUN mv /usr/local/etc/haproxy/haproxy.cfg
/usr/local/etc/haproxy/haproxy.cfg.orig  
  
RUN mkdir /config  
RUN ln -s /config/haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg  
  
VOLUME /config  
  
ENTRYPOINT ["/bootstrap-pre.sh"]  

