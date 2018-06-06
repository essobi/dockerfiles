FROM choko/mesos  
  
ADD http://downloads.mesosphere.io/marathon/v0.7.3/marathon-0.7.3.tgz
/tmp/marathon.tgz  
RUN mkdir -p /opt/marathon && tar xzf /tmp/marathon.tgz -C /opt/marathon
\--strip=1 && rm -f /tmp/marathon.tgz  
  
EXPOSE 8080  
CMD /opt/marathon/bin/start  

