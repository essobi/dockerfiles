# Marathon  
FROM thefactory/mesos:0.20.0  
MAINTAINER Mike Babineau mike@thefactory.com  
  
# Download Marathon  
ADD http://downloads.mesosphere.io/marathon/v0.7.0-RC2/marathon-0.7.0-RC2.tgz
/tmp/marathon.tgz  
RUN mkdir -p /opt/marathon && tar xzf /tmp/marathon.tgz -C /opt/marathon
--strip=1 && rm -f /tmp/marathon.tgz  
  
USER root  
EXPOSE 8080  
ENTRYPOINT ["/opt/marathon/bin/start"]  

