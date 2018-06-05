FROM debian:wheezy  
  
RUN apt-get update \  
&& apt-get install -y openjdk-7-jre-headless \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD
https://download.elasticsearch.org/logstash/logstash/packages/debian/logstash_1.4.2-1-2c0f5a1_all.deb
/root/logstash.deb  
  
WORKDIR /root  
  
RUN dpkg -i logstash.deb \  
&& rm /root/logstash.deb  
  
VOLUME /etc/opt/logstash  
  
EXPOSE 514  
EXPOSE 9292  
CMD ["/opt/logstash/bin/logstash", "agent", "-f",
"/etc/opt/logstash/logstash.conf", "web"]  

