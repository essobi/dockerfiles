FROM registry.fedoraproject.org/fedora:27  
ENV LANG C.UTF-8  
RUN dnf -y update && rm -rf /usr/share/doc /usr/share/man /var/cache/dnf  
RUN dnf -y install java-1.8.0-openjdk-headless mongodb-server unzip && rm -rf
/usr/share/doc /usr/share/man /var/cache/dnf  
  
RUN mkdir /data /logs /opt/UniFi  
RUN ln -s /data /opt/UniFi/data  
RUN ln -s /logs /opt/UniFi/logs  
  
ADD https://dl.ubnt.com/unifi/5.8.16-3e768cadb8/UniFi.unix.zip
/tmp/UniFi.unix.zip  
ADD https://dl.ubnt.com/unifi/5.8.16-3e768cadb8/unifi_sh_api
/usr/local/bin/unifi_sh_api  
  
RUN chmod a+x /usr/local/bin/unifi_sh_api  
  
RUN unzip /tmp/UniFi.unix.zip -d /opt  
  
RUN rm -rf /tmp/*  
  
VOLUME /data  
VOLUME /logs  
  
EXPOSE 1900/udp  
EXPOSE 3478/udp  
EXPOSE 5353/udp  
EXPOSE 6789/tcp  
EXPOSE 8080/tcp  
EXPOSE 8443/tcp  
EXPOSE 8843/tcp  
EXPOSE 8880/tcp  
EXPOSE 10001/udp  
  
WORKDIR /opt/UniFi  
  
CMD ["java", "-jar", "lib/ace.jar", "start"]  
  
# Local Variables:  
# indent-tabs-mode: nil  
# End:  

