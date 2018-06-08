FROM debian:8  
MAINTAINER Pascal Rinker <info@kronova.net>  
  
RUN apt-get update && apt-get -y install openvpn easy-rsa && \  
cp /usr/share/doc/openvpn/examples/sample-config-files/server.conf.gz
/etc/openvpn/ && \  
gunzip /etc/openvpn/server.conf.gz && cd /etc/openvpn && mkdir easy-rsa/ && \  
cp -R /usr/share/easy-rsa/* easy-rsa/ && mkdir /opt/certs/ && mkdir log/ mkdir
/opt/kronovanet_docker/  
  
VOLUME ["/etc/openvpn/easy-rsa/keys"]  
VOLUME ["/opt/kronovanet_docker"]  
  
EXPOSE 1194/udp  
EXPOSE 443/tcp  
  
ENV OPENVPN_HOSTNAME localhost  
  
COPY ./bin /usr/local/bin/  
COPY ./config /etc/openvpn/  
RUN chmod a+x /usr/local/bin/kronova_openvpn  
RUN chmod a+x /usr/local/bin/verify_user  
  
CMD ["/usr/local/bin/kronova_openvpn"]

