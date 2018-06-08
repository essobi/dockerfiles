FROM openshift/base-centos7  
  
MAINTAINER Martin Rumanek <martin@rumanek.cz>  
ENV GRADLE_VERSION=2.12  
ENV TOMCAT_MAJOR 8  
ENV TOMCAT_VERSION 8.0.38  
ENV CATALINA_HOME /usr/local/tomcat  
ENV JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8  
ENV TOMCAT_TGZ_URL
https://archive.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz  
  
RUN curl -v -j -k -fsL -H "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.rpm
> /tmp/jdk-8u131-linux-x64.rpm && \  
rpm -Uvh /tmp/jdk-8u131-linux-x64.rpm && \  
rm /tmp/jdk-8u131-linux-x64.rpm  
  
WORKDIR $CATALINA_HOME  
  
RUN curl -fSL "$TOMCAT_TGZ_URL" -o tomcat.tar.gz && \  
tar -xvf tomcat.tar.gz --strip-components=1 && \  
rm bin/*.bat && \  
rm tomcat.tar.gz*  
  
# SOLR  
RUN curl -sL
https://github.com/ceskaexpedice/kramerius/releases/download/v5.1.0/Installation-5.1.zip
-o /tmp/installation.zip  
ENV SOLR_HOME /usr/local/solr  
RUN unzip /tmp/installation.zip -d /tmp/  
RUN cp /tmp/Installation-5.1/solr.war $CATALINA_HOME/webapps/solr.war && \  
cp -r /tmp/Installation-5.1/solr $SOLR_HOME  
  
ENV SOLR_HOME /usr/local/solr  
ENV JAVA_OPTS -Djava.awt.headless=true -Dfile.encoding=UTF8
-XX:MaxPermSize=256m -Xms1024m -Xmx3072m
-Djava.security.auth.login.config=$JAAS_CONFIG -Dsolr.solr.home=$SOLR_HOME  
  
  
EXPOSE 8080  
CMD ["/usr/local/tomcat/bin/catalina.sh", "run"]  

