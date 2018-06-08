# Use metricbeat base for management  
# centos:7 is base of it  
FROM docker.elastic.co/beats/metricbeat:5.5.0  
#labels  
LABEL maintainer "emmanuel.lesne@middleware-solutions.fr"  
LABEL version="1.0"  
LABEL description="Image of wildfly server. It should be used like a base for
application image."  
LABEL fr.middlewaresolutions.wildfly.version="10.1.0.Final"  
LABEL fr.middlewaresolutions.jdk.version="OpenJDK-8"  
  
# Set the WILDFLY_VERSION env variable  
ENV WILDFLY_VERSION 10.1.0.Final  
# Set the JBOSS_HOME env variable  
ENV WILDFLY_HOME /opt/jboss/wildfly  
ENV JAVA_VERSION 1.8.0  
#ENV JAVA_OPTS -Xms64m -Xmx256m -XX:MetaspaceSize=96M
-XX:MaxMetaspaceSize=256m -Djava.net.preferIPv4Stack=true  
ENV JAVA_HOME /usr/lib/jvm/java-$JAVA_VERSION  
  
ENV METRICBEAT_HOME /usr/share/metricbeat/  
ENV LOGSTASH_HOME /usr/share/logstash/  
  
# Metricbeat parameters  
ENV ELASTICSEARCH_HOST elasticsearch-elastic.minishift.local:80  
ENV ELASTICSEARCH_USER elastic  
ENV ELASTICSEARCH_PWD changeme  
ENV APPLICATION_NAME wildfly  
ENV APPLICATION_VERSION 1.0  
ENV ENVIRONMENT dev  
  
USER root  
  
RUN yum -y upgrade && \  
yum -y install java-$JAVA_VERSION-openjdk-devel  
  
##################################  
# Elastic MetricBeat agent  
##################################  
USER root  
  
# Add metricbeat configuration  
ADD metricbeat/* $METRICBEAT_HOME  
RUN chmod u+x $METRICBEAT_HOME/*.sh  
  
##################################  
# Elastic Logstash agent  
##################################  
USER root  
  
ADD logstash/*.repo /etc/yum.repos.d/  
  
RUN rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch && \  
yum -y install logstash  
  
# copy  
ADD logstash/*.conf $WILDFLY_HOME/  
  
##################################  
# wildfly  
##################################  
# USER wildfly  
# Add the WildFly distribution to /opt, and make wildfly the owner of the
extracted tar content  
# Make sure the distribution is available from a well-known place  
RUN cd /tmp && \  
mkdir /opt/jboss -p && \  
curl
http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
| tar zx && \  
mv wildfly-* $WILDFLY_HOME  
  
# add all content for wildfly  
ADD wildfly/ $WILDFLY_HOME/  
RUN chmod u+x $WILDFLY_HOME/*.sh  
  
# Expose the ports we're interested in  
EXPOSE 8080 9990  
# Set the default command to run on boot  
# This will boot WildFly in the standalone mode and bind to all interface  
CMD ["/opt/jboss/wildfly/start.sh"]  

