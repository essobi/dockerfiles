FROM ubuntu:16.04  
  
ENV JBOSS_HOME /opt/jboss/jboss-eap-6.4  
  
### copy config  
COPY config /config  
  
RUN groupadd jboss \  
&& useradd -m -g jboss jboss \  
#Install util tools  
&& apt-get update \  
&& apt-get install wget -y \  
#JDK install  
&& apt-get install openjdk-8-jdk -y \  
#EAP install  
&& mkdir -p /opt/jboss \  
&& cd /opt/jboss/ \  
&& wget -O jboss-eap-6.4.tar.gz -N
"https://svc.integracion.euskadi.net/y31ApiJSWAR/Y31JanoServiceGetServlet?hadoop_file_path=/user/jbarbarb/jboss-
eap-6.4.tar.gz&xlnets_token=5d2d94b9-273d-4f47-9697-91b77387a05a" \  
&& tar -xvzf jboss-eap-6.4.tar.gz \  
&& rm -rf /opt/jboss/jboss-eap-6.4.tar.gz \  
&& chmod 775 /opt/jboss/jboss-eap-6.4/bin/add-user.sh \  
&& $JBOSS_HOME/bin/add-user.sh admin admin123! --silent \  
&& echo "JAVA_OPTS=\"\$JAVA_OPTS -Djboss.bind.address=0.0.0.0
-Djboss.bind.address.management=0.0.0.0\"" >> $JBOSS_HOME/bin/standalone.conf  
  
### Open Ports  
EXPOSE 80 8080 9990  
  
RUN mkdir -p $JBOSS_HOME/modules/config/main && \  
echo "<?xml version="1.0" encoding="UTF-8"?><module name="config"
xmlns="urn:jboss:module:1.1"><resources><resource-root
path="."/></resources></module>" >> $JBOSS_HOME/modules/config/main/module.xml  
  
### create WAR  
ADD sample /tmp/sample  
RUN cd /tmp/sample \  
&& jar -cvf sample.war -C /tmp/sample/ . \  
&& cp sample.war $JBOSS_HOME/standalone/deployments/sample.war  
# && chown -R jboss:jboss /opt/jboss /config \  
# && chmod -R 777 /opt/jboss /config  
  
RUN chgrp -R 0 /opt/jboss && chmod -R g+rw /opt/jboss && find /opt/jboss -type
d -exec chmod g+x {} +  
RUN chgrp -R 0 /config && chmod -R g+rw /config && find /config -type d -exec
chmod g+x {} +  
  
ENTRYPOINT /bin/bash -c "$JBOSS_HOME/bin/standalone.sh -c standalone-full-
ha.xml -Djboss.node.name=server1"  

