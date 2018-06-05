FROM bailaohe/java:7  
MAINTAINER He Bai <bai.he@outlook.com>  
  
RUN curl -SL
https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.5.2.tar.gz
| tar -xzC /opt  
RUN curl -SL https://github.com/medcl/elasticsearch-analysis-
ik/archive/master.tar.gz | tar -xzC /opt  
  
WORKDIR /opt/elasticsearch-analysis-ik-master  
RUN mvn package  
  
ENV ESDIR /opt/elasticsearch-1.5.2  
ENV IKDIR /opt/elasticsearch-analysis-ik-master  
WORKDIR /opt  
RUN cp ${IKDIR}/target/releases/elasticsearch-analysis-ik-*-jar-with-
dependencies.jar ${ESDIR}/lib/  
RUN cp -r ${IKDIR}/config/elasticsearch.yml ${ESDIR}/config/  
RUN cp -r ${IKDIR}/config/ik ${ESDIR}/config/  
  
EXPOSE 9200/tcp 9300/udp  
CMD ${ESDIR}/bin/elasticsearch  

