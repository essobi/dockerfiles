FROM ubuntu:latest  
MAINTAINER José Luis Salvador Rufo <salvador.joseluis@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV PATH /usr/share/elasticsearch/bin:$PATH  
  
ADD
http://packages.elasticsearch.org/elasticsearch/0.90/debian/pool/main/e/elasticsearch/elasticsearch-0.90.13.deb
/tmp/  
ADD https://github.com/tianon/gosu/releases/download/1.6/gosu-amd64
/usr/local/bin/gosu  
COPY docker-entrypoint.sh /  
COPY logging.yml /usr/share/elasticsearch/config/  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections && \  
apt-get update -q && \  
apt-get install --no-install-recommends -qy openjdk-8-jdk && \  
dpkg -i /tmp/elasticsearch-0.90.13.deb && \  
chmod +x /usr/local/bin/gosu && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME /usr/share/elasticsearch/data  
  
EXPOSE 9200 9300  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["elasticsearch"]  

