# From alpine:latest image  
FROM alpine:latest  
  
# Set the maintainer  
MAINTAINER Mike  
  
# Set work dir  
WORKDIR /opt/src  
  
# Install dep packge , Configure,make and install strongSwan  
RUN apk --no-cache --update add wget bash iproute2 iptables openssl kmod
libreswan xl2tpd ipsec-tools \  
&& rm -f /etc/ppp/chap-secrets /etc/ipsec.d/passwd /etc/ipsec.secrets  
  
# Copy start file  
COPY ./run.sh /opt/src/run.sh  
  
# Copy helper files  
COPY ./adduser.sh /opt/src/adduser.sh  
COPY ./lsusers.sh /opt/src/lsusers.sh  
COPY ./rmuser.sh /opt/src/rmuser.sh  
  
# Set permissions  
RUN chmod 755 /opt/src/run.sh /opt/src/adduser.sh /opt/src/lsusers.sh
/opt/src/rmuser.sh  
  
# Open ports  
EXPOSE 500:500/udp 4500:4500/udp  
  
# Mount volumnes  
VOLUME ["/lib/modules", "/etc/ppp/chap-secrets", "/etc/ipsec.d/passwd",
"/etc/ipsec.secrets"]  
  
# Start  
CMD ["/opt/src/run.sh"]  

