FROM pataquets/solr:4.10.4  
ADD files/entrypoint.sh /entrypoint.sh  
ADD files/etc/default/solr /etc/default/solr  
ADD files/opt/solr/example/solr/collection1/conf
/opt/solr/example/solr/collection1/conf/  
  
# JAVA  
ENV JAVA_MAJOR 8  
ENV JAVA_MINOR 74  
COPY files/server-jre-${JAVA_MAJOR}u${JAVA_MINOR}-linux-x64.tar.gz
/tmp/server-jre-${JAVA_MAJOR}u${JAVA_MINOR}-linux-x64.tar.gz  
RUN tar -zvxf /tmp/server-jre-${JAVA_MAJOR}u${JAVA_MINOR}-linux-x64.tar.gz -C
/opt  
RUN rm /usr/bin/java  
RUN ln -s /opt/jdk/bin/java /usr/bin/java  
RUN rm /tmp/server-jre-${JAVA_MAJOR}u${JAVA_MINOR}-linux-x64.tar.gz  
  
ENTRYPOINT [ "/entrypoint.sh" ]  

