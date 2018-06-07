FROM iotsec/arm-alpine  
  
RUN apk --update add bridge \  
hostapd \  
wireless-tools \  
wpa_supplicant \  
nftables \  
openrc &&\  
rc-update add nftables &&\  
rm -rf /var/cache/apk/*  
  
CMD ip link set dev $AP_IFACE up && hostapd /etc/hostapd/hostapd.conf  

