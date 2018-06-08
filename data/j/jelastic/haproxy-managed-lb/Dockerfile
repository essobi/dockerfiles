FROM haproxy  
  
ENV HOSTS_PORT=80  
ADD config/haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg  
ADD config/lb_manager.sh /root/lb_manager.sh  
RUN chmod +x /root/lb_manager.sh  

