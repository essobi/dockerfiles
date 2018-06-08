FROM java:7-jre  
ENV ES_VERSION 1.1.2  
ENV PATH /bin:/usr/bin:/sbin:/usr/sbin:/app/bin  
RUN mkdir /app && wget -O -
"https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-$ES_VERSION.tar.gz"
| tar xzf - -C /app --strip-components 1  
ADD run.sh /run.sh  
ADD elasticsearch.yml /app/config/elasticsearch.yml  
VOLUME ["/data"]  
WORKDIR /data  
EXPOSE 9200  
EXPOSE 9300  
CMD ["/run.sh"]  

