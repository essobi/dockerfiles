FROM macedigital/jre-server  
  
COPY elasticsearch.repo /etc/yum.repos.d/  
RUN rpm --import https://packages.elastic.co/GPG-KEY-elasticsearch \  
&& yum -y install elasticsearch \  
&& yum clean all  
  
ENV PATH /usr/share/elasticsearch/bin:$PATH  
ENV ES_USER elasticsearch  
ENV ES_HOME /usr/share/elasticsearch  
ENV LOG_DIR /var/log/elasticsearch  
ENV DATA_DIR /var/lib/elasticsearch  
ENV CONF_DIR /etc/elasticsearch  
  
WORKDIR /usr/share/elasticsearch  
  
COPY run.sh /usr/share/elasticsearch/bin/  
  
USER elasticsearch  
  
VOLUME [ "/usr/share/elasticsearch/conf", "/var/lib/elasticsearch/data" ]  
  
EXPOSE 9200 9300  
CMD [ "/usr/share/elasticsearch/bin/run.sh" ]  

