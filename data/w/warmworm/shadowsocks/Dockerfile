FROM mritd/shadowsocks:3.0.6  
ENV RUN_DEPD supervisor curl dnsmasq py-pip nginx  
  
RUN apk add --no-cache $RUN_DEPD && \  
pip install --no-cache-dir
https://github.com/JinnLynn/genpac/archive/master.zip  
  
  
COPY ./files /  
  
#8000 for server: server port  
EXPOSE 8000/tcp  
EXPOSE 8000/udp  
  
#1080/tcp for local : socks5 proxy  
#53/udp for local : dns server with ipset and gfwlist  
#80/tcp for local : auto proxy pac file  
EXPOSE 1080/tcp  
EXPOSE 53/udp  
EXPOSE 80/tcp  
  
ENTRYPOINT ["/entrypoint.sh"]  
  

