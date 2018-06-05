# Browser Mob Proxy  
FROM phusion/baseimage:0.9.15  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get -y install curl zip openjdk-7-jre-headless \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN curl -SL "https://github.com/lightbody/browsermob-
proxy/releases/download/browsermob-proxy-2.1.0-beta-2/browsermob-
proxy-2.1.0-beta-2-bin.zip" -o "/browsermob-proxy.zip" \  
&& unzip -q /browsermob-proxy.zip \  
&& rm -f /browsermob-proxy.zip  
  
RUN mkdir /etc/service/browsermob-proxy  
ADD run-browsermob-proxy.sh /etc/service/browsermob-proxy/run  
  
# 100 ports for listeners  
EXPOSE 9090-9191  

