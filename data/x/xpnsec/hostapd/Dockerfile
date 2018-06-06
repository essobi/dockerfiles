FROM kalilinux/kali-linux-docker  
  
# install base tools  
RUN apt-get update && apt-get install -y hostapd dnsmasq gettext-base  
  
ADD ./conf/start.sh /start.sh  
  
CMD ["/start.sh"]  

