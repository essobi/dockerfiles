# Chronos  
#  
# VERSION 2  
FROM thefactory/mesos  
  
MAINTAINER Federico Feroldi fferoldi@measurence.com  
  
# Download Chronos  
ADD
http://downloads.mesosphere.io.s3.amazonaws.com/chronos/chronos-2.1.0_mesos-0.14.0-rc4.tgz
/tmp/chronos.tgz  
RUN mkdir -p /opt/chronos && tar xzf /tmp/chronos.tgz -C /opt/chronos
--strip=2 && rm -f /tmp/chronos.tgz  
  
USER root  
EXPOSE 8080  
ENTRYPOINT ["/opt/chronos/bin/start-chronos.bash"]  

