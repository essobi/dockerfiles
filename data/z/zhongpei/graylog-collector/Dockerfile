FROM ubuntu:14.04  
  
RUN apt-get update \  
&& apt-get install -y wget\  
&& wget https://packages.graylog2.org/repo/packages/graylog-collector-latest-
repository-ubuntu14.04_latest.deb -O /tmp/graylog-collector.deb\  
&& dpkg -i /tmp/graylog-collector.deb\  
&& apt-get install -y apt-transport-https\  
&& apt-get update\  
&& apt-get install -y graylog-collector\  
&& apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
  
CMD ["bin/graylog-collector", "run", "-f", "/collector.conf"]  

