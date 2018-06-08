FROM debian:8  
LABEL maintainer="Cyrius, Celforyon"  
LABEL version="1.0"  
LABEL description="Simple vpn server using openvpn."  
  
RUN echo "deb http://swupdate.openvpn.net/apt jessie main" >
/etc/apt/sources.list.d/swupdate-openvpn.list  
  
RUN apt-get update && apt-get install -y wget  
RUN wget -O - https://swupdate.openvpn.net/repos/repo-public.gpg | apt-key add
-  
RUN apt-get update && apt-get install -y \  
ca-certificates \  
iptables \  
openssl \  
openvpn \  
supervisor \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo 'net.ipv4.ip_forward=1' >> /etc/sysctl.conf  
  
VOLUME ["/etc/openvpn"]  
VOLUME ["/cert"]  
  
EXPOSE 1194/udp  
  
ENV CIPHER="cipher AES-256-CBC"  
ENV DH_KEY_SIZE=2048  
ENV RSA_KEY_SIZE=2048  
ENV DNS=1  
ENV PROTOCOL=udp  
ENV EXTERNAL_PORT=1194  
ADD bin /usr/local/bin  
ADD ./supervisord.conf /root  
COPY EasyRSA-3.0.1.tgz /root  
CMD ovpn_run  

