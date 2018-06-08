FROM cusspvz/openwrt:15.05-x64  
  
EXPOSE 80  
RUN uci delete network.lan && \  
uci delete network.wan && \  
uci delete network.wan6 && \  
uci delete dhcp.lan && \  
uci commit  
  
CMD ["/sbin/procd", "-"]  

