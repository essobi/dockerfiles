FROM alpine  
  
COPY start.sh /root/  
  
RUN apk add --no-cache ca-certificates squid openvpn openssl && \  
update-ca-certificates && \  
chmod +x /root/*.sh  
  
COPY squid.conf /etc/squid/  
  
VOLUME /config  
  
EXPOSE 3128  
CMD ["/root/start.sh"]  

