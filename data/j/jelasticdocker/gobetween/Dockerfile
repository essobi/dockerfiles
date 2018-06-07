#  
FROM yyyar/gobetween  
  
RUN mkdir -p /etc/gobetween/conf  
ADD config/gobetween.toml /etc/gobetween/conf/gobetween.toml  
ADD bin/lb_manager.sh /root/lb_manager.sh  
RUN chmod +x /root/lb_manager.sh  
  

