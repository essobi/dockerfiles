FROM 221robotics/armv7hf-debian-qemu  
  
RUN [ "cross-build-start" ]  
  
COPY stretch.list /etc/apt/sources.list.d/stretch.list  
COPY default-release /etc/apt/apt.conf.d/default-release  
  
RUN apt-get update && \  
apt-get install -y -t stretch dnsmasq hostapd network-manager rng-tools && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
COPY hostapd.conf /etc/hostapd/hostapd.conf  
COPY dnsmasq.conf /etc/dnsmasq.conf  
COPY start_ap.sh /usr/bin/start_ap.sh  
  
RUN echo "RUN_DAEMON=\"yes\"\nDAEMON_CONF=\"/etc/hostapd/hostapd.conf\"" >>
/etc/default/hostapd  
RUN chmod u+x /usr/bin/start_ap.sh  
  
CMD ["/usr/bin/start_ap.sh"]  
  
RUN [ "cross-build-end" ]  

