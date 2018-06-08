FROM debian:stretch  
MAINTAINER František Dvořák <valtri@civ.zcu.cz>  
  
ENV v 3.7.1  
  
EXPOSE 8009 8080  
  
WORKDIR /root  
  
# graphviz - for GUI features  
# xlmstaret - for docker image scripts  
# tomcat8 additional packages (to prevent warnings), native package  
RUN apt-get update && apt-get install -y --no-install-recommends \  
gzip \  
graphviz \  
libmysql-java \  
mc \  
openjdk-8-jdk \  
tomcat8 libservlet3.1-java libcommons-dbcp-java libcommons-pool-java
libtcnative-1 \  
wget \  
xmlstarlet \  
&& rm -rf /var/lib/apt/lists/*  
# mc (cosmetics)  
RUN mkdir -p ~/.config/mc/ \  
&& echo 'ENTRY "/var/lib/tomcat8/webapps/midpoint/WEB-INF" URL
"/var/lib/tomcat8/webapps/midpoint/WEB-INF"' >> ~/.config/mc/hotlist \  
&& echo 'ENTRY "/var/log/tomcat8" URL "/var/log/tomcat8"' >>
~/.config/mc/hotlist \  
&& echo 'ENTRY "/var/opt/midpoint" URL "/var/opt/midpoint"' >>
~/.config/mc/hotlist \  
&& ln -s /usr/lib/mc/mc.csh /etc/profile.d/ \  
&& ln -s /usr/lib/mc/mc.sh /etc/profile.d/  
  
# tomcat  
RUN service tomcat8 stop \  
&& echo 'JAVA_OPTS="${JAVA_OPTS} -Xms256m -Xmx1024m -Xss1m
-Dmidpoint.home=/var/opt/midpoint
-Djavax.net.ssl.trustStore=/var/opt/midpoint/keystore.jceks
-Djavax.net.ssl.trustStoreType=jceks"' >> /etc/default/tomcat8 \  
&& sed -i '/Service name="Catalina".*/a \\\n <Connector port="8009"
protocol="AJP/1.3"/>' /etc/tomcat8/server.xml  
RUN mkdir /var/opt/midpoint \  
&& chown tomcat8:tomcat8 /var/opt/midpoint  
  
# midpoint  
RUN wget -nv
https://evolveum.com/downloads/midpoint/${v}/midpoint-${v}-dist.tar.gz \  
&& tar xzf midpoint-${v}-dist.tar.gz \  
&& rm -fv midpoint-${v}-dist.tar.gz  
  
# deployment  
# (tomcat8 startup is OK, but returns non-zero code)  
RUN service tomcat8 start || : \  
&& cp -vp midpoint-${v}/lib/midpoint.war /var/lib/tomcat8/webapps/ \  
&& rm -rf midpoint-${v}/ \  
&& while ! test -f /var/opt/midpoint/config.xml; do sleep 0.5; done \  
&& sleep 60 \  
&& service tomcat8 stop  
RUN ln -L /usr/share/java/mysql-connector-java.jar /var/lib/tomcat8/lib/  
RUN wget -nv -P /var/opt/midpoint/icf-connectors/
http://nexus.evolveum.com/nexus/content/repositories/openicf-
releases/org/forgerock/openicf/connectors/scriptedsql-
connector/1.1.2.0.em3/scriptedsql-connector-1.1.2.0.em3.jar  
  
RUN rm -fv /var/opt/midpoint/midpoint*.db /var/log/tomcat8/* \  
&& rm -rfv /var/lib/tomcat8/webapps/ROOT/ /var/lib/tomcat/work/Catalina/  
  
COPY docker-entry.sh /  
CMD /docker-entry.sh /bin/bash -l  

