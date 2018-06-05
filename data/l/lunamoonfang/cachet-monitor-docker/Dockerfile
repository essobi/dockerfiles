FROM debian:stable  
  
MAINTAINER Thomas Wiringa "thomas.wiringa@gmail.com"  
ENV CACHET_MONITOR_VERSION v2.0  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
wget \  
ca-certificates  
  
RUN wget https://github.com/CastawayLabs/cachet-
monitor/releases/download/$CACHET_MONITOR_VERSION/cachet-monitor_linux_amd64 \  
&& mv cachet-monitor_linux_amd64 /usr/local/bin/cachet-monitor \  
&& chmod +x /usr/local/bin/cachet-monitor  
  
RUN apt-get remove -y \  
wget \  
ca-certificates \  
&& apt-get -y clean \  
&& apt-get -y autoremove  
  
COPY cachet-monitor.config.json /etc/cachet-monitor.config.json  
  
ENTRYPOINT ["/usr/local/bin/cachet-monitor", "-c", "/etc/cachet-
monitor.config.json"]  

