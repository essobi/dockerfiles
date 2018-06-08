FROM bitnami/minideb:stretch  
LABEL maintainer="Dominik Mähl <dominik@maehl.eu>"  
  
VOLUME ["/var/lib/unifi", "/var/log/unifi", "/var/run/unifi"]  
  
#UniFi Ports (https://help.ubnt.com/hc/en-us/articles/218506997-UniFi-Ports-
Used)  
EXPOSE 8080/tcp 8443/tcp 8880/tcp 8843/tcp 6789/tcp 3478/udp 10001/udp  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#install needed packages  
RUN install_packages curl mongodb-server libcap2 ca-certificates binutils jsvc  
  
#install oracle jdk  
RUN curl -OLS -H "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jdk/8u171-b11/512cd62ec5174c3487ac17c61aaa89e8/jdk-8u171-linux-x64.tar.gz
\  
&& mkdir /opt/jdk \  
&& tar xvzf jdk-8u171-linux-x64.tar.gz --strip 1 -C /opt/jdk \  
&& rm jdk-8u171-linux-x64.tar.gz  
  
#install UniFi Controller  
RUN curl -OLS
https://dl.ubnt.com/unifi/5.9.4-b647df56b7/unifi_sysvinit_all.deb \  
&& dpkg --force-all -i unifi_sysvinit_all.deb \  
&& rm unifi_sysvinit_all.deb  
  
#let UniFi use the volumes  
RUN ln -s /var/lib/unifi /usr/lib/unifi/data \  
&& ln -s /var/log/unifi /usr/lib/unifi/logs \  
&& ln -s /var/run/unifi /usr/lib/unifi/run  
#correct wd is necessary because unifi places its log in .\logs\server.log  
WORKDIR /usr/lib/unifi  
  
ENTRYPOINT ["/opt/jdk/bin/java", "-Xmx1024M", "-jar",
"/usr/lib/unifi/lib/ace.jar"]  
CMD ["start"]  

