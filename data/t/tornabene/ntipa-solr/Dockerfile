# NTIPA-SOLR 0.0.1  
FROM ubuntu:trusty  
MAINTAINER Tindaro Tornabene <tindaro.tornabene@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
RUN apt-get -y -q install python-software-properties software-properties-
common  
RUN apt-get install -yqq inetutils-ping net-tools  
  
# install oracle java from PPA  
RUN add-apt-repository ppa:webupd8team/java -y  
RUN apt-get update  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get -y install oracle-java7-installer && apt-get clean  
  
# Set oracle java as the default java  
RUN update-java-alternatives -s java-7-oracle  
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-7-oracle" >> ~/.bashrc  
  
ENV SOLR solr-4.10.4  
WORKDIR /opt  
RUN wget http://it.apache.contactlab.it/lucene/solr/4.10.4/solr-4.10.4.tgz -O
/opt/$SOLR.tgz  
  
RUN ls -lah /opt  
RUN tar -C /opt --extract --file /opt/$SOLR.tgz  
RUN ln -s /opt/$SOLR /opt/solr  
  
WORKDIR /opt/solr/example/solr  
RUN cp -r collection1/ ntipa/  
  
WORKDIR /opt/solr/example/solr/ntipa  
RUN echo "name=ntipa" > core.properties  
RUN cat core.properties  
  
ADD schema.xml /opt/solr/example/solr/ntipa/conf/schema.xml  
RUN rm -f /opt/solr/example/solr/ntipa/data/*  
  
EXPOSE 8983  
WORKDIR /opt/solr/example  
CMD /usr/bin/java -Xmx1024m -Dsolr.clustering.enabled=true -jar
/opt/solr/example/start.jar  

