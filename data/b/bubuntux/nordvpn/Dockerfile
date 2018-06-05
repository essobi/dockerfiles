FROM resin/armhf-alpine:3.7  
LABEL maintainer="Julio Gutierrez <bubuntux@gmail.com>"  
  
COPY nordVpn.sh /usr/bin  
CMD nordVpn.sh  
  
HEALTHCHECK \--start-period=5s --timeout=15s --interval=60s \  
CMD curl -fL 'https://api.ipify.org' || exit 1  
  
RUN ["cross-build-start"]  
# Install dependencies  
RUN apk --no-cache --no-progress upgrade && \  
apk --no-cache --no-progress add curl unzip iptables ip6tables jq openvpn && \  
# Download ovpn files  
curl https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip -o
/tmp/ovpn.zip && \  
unzip -q /tmp/ovpn.zip -d /tmp/ovpn && \  
mkdir -p /vpn/ovpn/ && \  
mv /tmp/ovpn/*/*.ovpn /vpn/ovpn/ && \  
# Cleanup  
rm -rf /tmp/*  
RUN ["cross-build-end"]  

