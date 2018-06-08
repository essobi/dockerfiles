FROM alpine:latest  
  
MAINTAINER Alexander Zinchenko <alexander@zinchenko.com>  
  
COPY nordVpn.sh /usr/bin  
  
HEALTHCHECK \--start-period=15s --timeout=15s --interval=60s \  
CMD curl -fL 'https://api.ipify.org' || exit 1  
  
ENV URL_NORDVPN_API="https://api.nordvpn.com/server" \  
URL_RECOMMENDED_SERVERS="https://nordvpn.com/wp-admin/admin-
ajax.php?action=servers_recommendations" \  
URL_OVPN_FILES="https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip"
\  
MAX_LOAD=70  
VOLUME ["/vpn/ovpn/"]  
  
# Install dependencies  
RUN apk --no-cache --no-progress update && \  
apk --no-cache --no-progress upgrade && \  
apk --no-cache --no-progress add bash curl unzip iptables ip6tables jq openvpn
tini && \  
mkdir -p /vpn/ovpn/  
  
ENTRYPOINT ["/sbin/tini", "--", "/usr/bin/nordVpn.sh"]

