FROM ubuntu:14.04  
# Adapted from raycoding/piggybank-solr-tomcat and geoblacklight/solr  
MAINTAINER Nikitas Tampakis <nikitas.tampakis@gmail.com>  
  
# Environment Variables  
ENV SOLR_VERSION 4.10.0  
ENV TOMCAT_VERSION 7.0.59  
ENV SOLR solr-$SOLR_VERSION  
ENV TOMCAT apache-tomcat-$TOMCAT_VERSION  
ENV SOLR_HOME /usr/lib/solr-home  
ENV TOMCAT_HOME /usr/lib/$TOMCAT  
ENV SOLR_ZK_CLI /usr/lib/solr-zk-cli  
  
RUN apt-get update && apt-get -y install \  
unzip \  
wget \  
default-jdk \  
git  
  
WORKDIR /usr/lib  
# Fetch Apache Tomcat  
RUN \  
wget -q -nc
http://archive.apache.org/dist/tomcat/tomcat-7/v$TOMCAT_VERSION/bin/$TOMCAT.zip
&& \  
unzip -q /usr/lib/$TOMCAT.zip -d /usr/lib  
# Fetch Solr  
RUN \  
wget -q -nc http://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/$SOLR.zip
&& \  
unzip -q /usr/lib/$SOLR.zip -d /usr/lib  
#Setting up Tomcat with Solr  
RUN \  
cp /usr/lib/$SOLR/dist/$SOLR.war /usr/lib/$TOMCAT/webapps/solr.war && \  
cp /usr/lib/$SOLR/example/lib/ext/* /usr/lib/$TOMCAT/lib/ && \  
mkdir -p $SOLR_HOME  
  
ADD apache_tomcat_setenv.sh /usr/lib/$TOMCAT/bin/setenv.sh  
ADD tomcat-users.xml /usr/lib/$TOMCAT/conf/tomcat-users.xml  
# Uncomment to change the default 8080 port - also change apache_tomcat_setenv
script  
# RUN sed -i s/8080/8983/g /usr/lib/$TOMCAT/conf/server.xml  
  
ADD solr.xml $SOLR_HOME/solr.xml  
  
#Setting Up ZooKeeper Command Line Interface provided by Solr  
RUN mkdir -p $SOLR_ZK_CLI  
RUN unzip -q /usr/lib/$SOLR/dist/$SOLR.war -d /tmp/solr-war  
RUN cp /tmp/solr-war/WEB-INF/lib/* $SOLR_ZK_CLI  
RUN cp /usr/lib/$SOLR/example/lib/ext/* $SOLR_ZK_CLI  
RUN rm -rf /tmp/solr-war  
  
#Setting Up Symlinks  
RUN ln -s $SOLR_HOME /solr-home  
RUN ln -s $TOMCAT_HOME /tomcat-home  
RUN ln -s /usr/lib/$SOLR /solr-dist  
RUN ln -s $SOLR_ZK_CLI /solr-zk-cli  
  
# Orangelight Specific SolrConfig  
RUN \  
git clone -b blacklight_511 https://github.com/pulibrary/orangelight.git && \  
mkdir $TOMCAT_HOME/conf/Catalina $TOMCAT_HOME/conf/Catalina/localhost && \  
echo '<Context docBase="/usr/lib/apache-tomcat-7.0.59/webapps/solr.war"
debug="0" crossContext="true" > \  
<Environment name="solr/home" type="java.lang.String" value="/solr-home"
override="true" /> \  
</Context>' > $TOMCAT_HOME/conf/Catalina/localhost/solr.xml && \  
mv /solr-dist/example/solr/collection1 /solr-home/blacklight-core && \  
sed -i s/collection1/blacklight-core/g /solr-home/blacklight-
core/core.properties && \  
cp -r orangelight/solr_conf/conf/* /solr-home/blacklight-core/conf && \  
rm -r orangelight && \  
mv /solr-home/blacklight-core/conf/lang/stopwords_en.txt /solr-
home/blacklight-core/conf && \  
mv /solr-dist/example/lib /solr-home && \  
mv /solr-dist/contrib /solr-home/lib  
  
RUN chmod 755 -R $SOLR_HOME  
RUN chmod +x /usr/lib/$TOMCAT/bin/*.sh  
EXPOSE 8080  
  
RUN rm -f /usr/lib/$SOLR.zip && rm -rf /usr/lib/$TOMCAT.zip

