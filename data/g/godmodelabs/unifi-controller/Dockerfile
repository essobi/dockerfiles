FROM debian:stable  
  
ADD https://dl.ubnt.com/unifi/unifi-repo.gpg /etc/apt/trusted.gpg.d/  
RUN chmod 644 /etc/apt/trusted.gpg.d/unifi-repo.gpg && \  
echo "deb http://www.ubnt.com/downloads/unifi/debian stable ubiquiti" >
/etc/apt/sources.list.d/ubnt.list && \  
apt-get update -q -y && \  
apt-get install -q -y mongodb-server unifi && \  
apt-get -q clean && rm -rf /var/lib/apt/lists/*  
  
VOLUME /usr/lib/unifi/data  
EXPOSE 8443 8880 8080  
WORKDIR /usr/lib/unifi  
CMD ["java", "-Xmx256M", "-jar", "/usr/lib/unifi/lib/ace.jar", "start"]  

