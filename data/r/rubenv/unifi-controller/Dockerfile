FROM debian  
  
RUN apt-get update && \  
apt-get install --no-install-recommends -qy gnupg2 dirmngr && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv C0A52C50 && \  
echo "deb http://www.ubnt.com/downloads/unifi/debian stable ubiquiti" >
/etc/apt/sources.list.d/100-ubnt.list && \  
apt-get update && \  
apt-get install --no-install-recommends -qy unifi && \  
apt-get -q clean && rm -rf /var/lib/apt/lists/* && \  
mkdir -p /var/lib/unifi && \  
ln -s /var/lib/unifi /usr/lib/unifi/data  
  
EXPOSE 8080/tcp 8081/tcp 8443/tcp 8843/tcp 8880/tcp 3478/udp  
VOLUME ["/var/lib/unifi"]  
WORKDIR /var/lib/unifi  
  
CMD ["java", "-Xmx256M", "-jar", "/usr/lib/unifi/lib/ace.jar", "start"]  

