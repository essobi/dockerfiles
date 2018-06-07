FROM ubuntu:latest  
  
COPY /home /root  
  
RUN apt-get update && apt-get install -y \  
autofs \  
samba \  
&& rm -rf /var/lib/apt/lists/* \  
&& echo '/mnt/iso_auto /etc/auto.isos --timeout=10' >> /etc/auto.master \  
&& echo '* -fstype=auto,loop,ro,uid=$USER :/mnt/raw_iso/&.iso' >
/etc/auto.isos \  
&& chmod 755 /root/start.sh \  
&& chmod 755 /root/symblink_isos.sh  
  
VOLUME [ "/mnt/raw_iso" ]  
VOLUME [ "/etc/samba" ]  
  
EXPOSE 137/udp 138/udp 139 445  
RUN mkdir -p /mnt/iso_auto \  
&& mkdir -p /share/iso \  
&& ln -s /mnt/raw_iso /share/raw_iso  
  
ENTRYPOINT ["/bin/bash"]  
CMD ["/root/start.sh"]  

