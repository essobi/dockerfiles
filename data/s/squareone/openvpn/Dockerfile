# Original credit: https://github.com/jpetazzo/dockvpn  
FROM debian:jessie  
  
RUN apt-get update && \  
apt-get install -y openvpn iptables && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Needed by scripts  
ENV OPENVPN /etc/openvpn  
  
VOLUME ["/etc/openvpn"]  
  
# Internally uses port 1194, remap using docker  
EXPOSE 1194/udp  
  
WORKDIR /etc/openvpn  
CMD ["ovpn_run"]  
  
ADD ./bin /usr/local/bin  
RUN chmod a+x /usr/local/bin/*  

