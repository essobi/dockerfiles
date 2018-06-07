FROM ubuntu:16.04  
  
RUN apt-get update && \  
apt-get install -y \  
binutils \  
jsvc \  
mongodb-server \  
openjdk-8-jre-headless \  
wget \  
&& apt-get clean all  
  
RUN cd /tmp && \  
wget http://dl.ubnt.com/unifi/5.6.26/unifi_sysvinit_all.deb && \  
dpkg -i unifi_sysvinit_all.deb && \  
rm unifi_sysvinit_all.deb  
  
VOLUME /var/lib/unifi  
  
EXPOSE 8443 6789 8843 8880 8080 10001/udp 34675/udp 3478/udp  
  
RUN ln -s /var/lib/unifi /usr/lib/unifi/data  
RUN ln -s /var/log/unifi /usr/lib/unifi/logs  
RUN ln -s /var/run/unifi /usr/lib/unifi/run  
  
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64  
  
USER unifi  
  
WORKDIR /usr/lib/unifi/  
  
CMD exec java -Xmx512M -jar /usr/lib/unifi/lib/ace.jar start  

