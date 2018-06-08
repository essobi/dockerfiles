FROM shift/java:8  
MAINTAINER Vincent Palmer <shift@someone.section.me>  
  
WORKDIR /srv  
RUN apt-get install wget \  
&& wget
https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.5.2.tar.gz
\  
&& tar xfvz elasticsearch-1.5.2.tar.gz \  
&& mv elasticsearch-1.5.2 elasticsearch \  
&& rm elasticsearch-1.5.2.tar.gz \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD files/elasticsearch.yml /srv/elasticsearch/config/elasticsearch.yml  
  
VOLUME /data  
  
CMD ["/srv/elasticsearch/bin/elasticsearch"]  
  
EXPOSE 9200 9300  

