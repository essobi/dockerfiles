FROM centos:latest  
  
RUN yum update -y && \  
yum install -y java-1.8.0-openjdk sudo tar which && \  
yum clean -y all  
  
RUN sed -i -e "s/Defaults requiretty.*/ #Defaults requiretty/g" /etc/sudoers  
  
ENV JAVA_HOME /usr/lib/jvm/java-1.8.0-openjdk.x86_64  
ENV PATH $JAVA_HOME/bin:$PATH  
  
ENV ES_PKG_NAME elasticsearch-2.2.0  
ADD
https://download.elasticsearch.org/elasticsearch/elasticsearch/$ES_PKG_NAME.tar.gz
/tmp/$ES_PKG_NAME.tar.gz  
RUN cd /tmp && \  
tar xzvf $ES_PKG_NAME.tar.gz && \  
mv $ES_PKG_NAME /opt/elasticsearch && \  
rm -f $ES_PKG_NAME.tar.gz  
  
RUN echo 'http.cors.enabled: true' >>
/opt/elasticsearch/config/elasticsearch.yml && \  
echo 'http.cors.allow-origin: "/.*/"' >>
/opt/elasticsearch/config/elasticsearch.yml  
  
EXPOSE 9200  
EXPOSE 9300  
ENTRYPOINT ["/opt/elasticsearch/bin/elasticsearch"]

