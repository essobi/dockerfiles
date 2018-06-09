FROM ffhef/debian-batman:8.3-2017.0  
MAINTAINER Nico - Freifunk Hennef <nico@freifunk-hennef.de>  
  
ENV TINC_NAME=unkown  
ENV TINC_ADDRESS_FAMILY=ipv4  
ENV TINC_DEVICE=/dev/net/tun  
ENV TINC_MODE=switch  
ENV TINC_CONNECT_TO=""  
ENV TINC_INTERFACE_MAC=""  
ENV TINC_CONFIG_APPEND=""  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >
/etc/apt/sources.list.d/jessie-backports.list && \  
apt-get update && apt-get -t jessie-backports install -y tinc && apt-get clean
&& \  
rm /etc/apt/sources.list.d/jessie-backports.list && rm -rf /var/lib/apt/lists
/tmp/* /var/tmp/*  
  
EXPOSE 655/tcp 655/udp  
VOLUME /etc/tinc/rsa_key.priv  
VOLUME /etc/tinc/rsa_key.pub  
VOLUME /etc/tinc/hosts/  
  
ADD /tinc.conf.in /etc/tinc/tinc.conf.in  
ADD /tinc-up /etc/tinc/tinc-up  
ADD /tinc-down /etc/tinc/tinc-down  
ADD /entrypoint.sh /  
  
ENTRYPOINT [ "/entrypoint.sh" ]  
CMD [ "-D", "-U", "nobody" ]

