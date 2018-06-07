FROM defensative/baseimage:production  
  
MAINTAINER DEFENSATIVE Docker Mantainers "docker-maint@defensative.com"  
ADD run.sh /usr/sbin/run.sh  
ADD smoke_test.py /usr/sbin/smoke_test.py  
  
RUN apt-get update && \  
apt-get install -y dnsmasq && \  
apt-get purge -y man && \  
apt-get clean autoclean && \  
apt-get autoremove -y && \  
(dpkg -l | grep ^rc | awk '{print $2}' | xargs dpkg -P || true) && \  
rm -Rf /tmp/* && \  
rm -Rf /var/lib/apt/lists/*.gz && \  
rm -Rf /var/lib/cache/* && \  
rm -Rf /var/lib/log/* && \  
rm -Rf /var/log/* && \  
rm -Rf /var/cache/* && \  
echo "cache-size=1000" >> /etc/dnsmasq.conf && \  
echo "log-facility=-" >> /etc/dnsmasq.conf  
  
VOLUME /host_resolvdir  
  
ENTRYPOINT ["/usr/sbin/run.sh"]  
  
CMD ["-d", "-u", "dnsmasq", "-r", "/host_resolvdir/resolv.conf", "-7",
"/etc/dnsmasq.d"]  

