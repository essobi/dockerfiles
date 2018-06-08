FROM alpine:3.4  
MAINTAINER Wei Gao<wei@gaofamily.org>  
  
ARG STRONGSWAN_VERSION=5.4.0  
  
RUN apk add \--no-cache strongswan \  
&& mkdir -p /config \  
&& mkdir -p /orig-config \  
&& mv /etc/ipsec.conf /orig-config/ \  
&& mv /etc/ipsec.d /orig-config/ \  
&& ln -snf /config/ipsec.conf /etc/ipsec.conf \  
&& ln -snf /config/ipsec.secrets /etc/ipsec.secrets \  
&& ln -snf /config/ipsec.d /etc/ipsec.d  
  
# Strongswan Configuration  
ADD ipsec.conf /config/ipsec.conf  
  
ADD run.sh /run.sh  
  
# The password is later on replaced with a random string  
ENV VPN_USER user  
ENV VPN_PASSWORD password  
ENV VPN_PSK password  
  
EXPOSE 4500/udp 500/udp  
  
VOLUME "/config"  
  
CMD ["/run.sh"]  

