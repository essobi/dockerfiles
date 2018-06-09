FROM gliderlabs/alpine:latest  
MAINTAINER jens@lea.io  
  
RUN apk add --no-cache strongswan xl2tpd ppp-daemon  
  
# TODO use the conf dir for conf files...  
# RUN mkdir -p /conf  
WORKDIR /app  
  
# Configuration  
COPY config/ipsec.conf /etc/ipsec.conf  
COPY config/strongswan.conf /etc/strongswan.conf  
COPY config/xl2tpd.conf /etc/xl2tpd/xl2tpd.conf  
COPY config/options.xl2tpd /etc/ppp/options.xl2tpd  
  
COPY run.sh /usr/local/bin/ipsec-runner  
COPY vpn_adduser /usr/local/bin/vpn_adduser  
COPY vpn_deluser /usr/local/bin/vpn_deluser  
COPY vpn_setpsk /usr/local/bin/vpn_setpsk  
COPY vpn_unsetpsk /usr/local/bin/vpn_unsetpsk  
COPY vpn_apply /usr/local/bin/vpn_apply  
COPY vpn_makeCerts /usr/local/bin/vpn_makeCerts  
  
# The password is later on replaced with a random string  
ENV VPN_USER user  
ENV VPN_PASSWORD password  
ENV VPN_PSK password  
  
VOLUME ["/etc/ipsec.d"]  
  
EXPOSE 4500/udp 500/udp 1701/udp  
  
# CMD ["which", "xl2tpd"]  
CMD ["ash", "/usr/local/bin/ipsec-runner"]  
  

