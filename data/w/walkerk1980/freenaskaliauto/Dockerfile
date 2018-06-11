#FROM walkerk1980/freenaskali:intermediate  
FROM kalilinux/kali-linux-docker:latest  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -o
Dpkg::Options::="--force-confnew" \--assume-yes -y --yes -f dist-upgrade &&
apt-get install -y openssh-server dnsutils nmap nano tcpdump screen tmux
tshark  
RUN /bin/sed -i s/"PermitRootLogin prohibit-password"/"PermitRootLogin yes"/
/etc/ssh/sshd_config  
RUN /bin/systemctl enable ssh  
RUN mv /usr/sbin/tcpdump /usr/bin/tcpdump #&& hash –r  
RUN apt-get clean  
EXPOSE 22  
EXPOSE 8834  
EXPOSE 9392  
LABEL org.freenas.interactive="true" \  
org.freenas.command="/bin/sh" \  
org.freenas.version="2" \  
org.freenas.upgradeable="false" \  
org.freenas.port-mappings="22:22/tcp" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="true" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/root\", \  
\"descr\": \"Presistance directory for roots home folder\" \  
} \  
]" \  

