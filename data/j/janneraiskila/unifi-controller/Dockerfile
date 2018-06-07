FROM debian  
  
RUN echo "deb http://www.ubnt.com/downloads/unifi/debian stable ubiquiti" \  
>> /etc/apt/sources.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv C0A52C50 && \  
apt-get update && \  
apt-get install -y unifi && \  
rm -rf /var/lib/apt/lists/*  
  
VOLUME /usr/lib/unifi/data  
EXPOSE 8080 8443 8880 8843  
WORKDIR /usr/lib/unifi  
CMD ["java", "-Xmx256M", "-jar", "/usr/lib/unifi/lib/ace.jar", "start"]  

