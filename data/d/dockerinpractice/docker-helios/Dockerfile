FROM ubuntu:14.04.2  
ENV UPD eval apt-get update  
ENV CLEAN eval apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN $UPD && \  
apt-get install -y apt-transport-https && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FB0ACEBA8887F477 && \  
echo "deb https://spotify.github.io/helios-apt helios main" >>
/etc/apt/sources.list && \  
$CLEAN  
  
RUN $UPD && \  
apt-get install -y helios helios-agent helios-master && \  
$CLEAN  

