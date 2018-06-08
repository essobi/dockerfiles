FROM java:8  
MAINTAINER Alexis Hassler <alexis.hassler@sewatech.fr>  
  
ENV WILDFLY_VERSION 9.0.2.Final  
  
USER root  
  
RUN groupadd jboss && useradd -g jboss jboss && \  
mkdir /home/jboss && chown -R jboss:jboss /home/jboss  
  
RUN (curl -skL
http://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz
| tar xfz -) && \  
rm -r /wildfly-$WILDFLY_VERSION/welcome-content && \  
mv /wildfly-$WILDFLY_VERSION /wildfly &&\  
chown -R jboss:jboss wildfly &&\  
/wildfly/bin/add-user.sh --silent alexis hassler  
  
USER jboss  
  
COPY html /wildfly/welcome-content  
COPY standalone-ha.xml /wildfly/standalone/configuration/standalone-ha.xml  
  
EXPOSE 8080 8009 9990  
ENTRYPOINT ["/wildfly/bin/standalone.sh"]  

