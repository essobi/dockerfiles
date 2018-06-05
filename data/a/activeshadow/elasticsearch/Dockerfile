FROM debian:wheezy  
  
RUN apt-get update \  
&& apt-get install -y openjdk-7-jre-headless \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.4.2.deb
/root/elasticsearch.deb  
  
WORKDIR /root  
  
RUN dpkg -i elasticsearch.deb \  
&& rm /root/elasticsearch.deb  
  
VOLUME /etc/elasticsearch  
  
EXPOSE 9200  
EXPOSE 9300  
CMD ["/usr/share/elasticsearch/bin/elasticsearch",
"-Des.http.cors.enabled=true", "--default.path.conf=/etc/elasticsearch"]  

