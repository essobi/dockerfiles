FROM isuper/java-oracle:jdk_latest  
MAINTAINER Sajid Momin <sajid.momin@gmail.com>  
RUN apt-get update && \  
apt-get install -y mysql-client && \  
apt-get install -y maven && \  
apt-get install -y git-all && \  
apt-get install -y wget && \  
apt-get install -y curl && \  
apt-get install -y vim  
ENV DOWNLOADS="/opt/downloads" \  
BUNDLES="/opt/downloads/bundles"  
RUN wget -P $DOWNLOADS
https://www.jahia.com/downloads/jahia/digitalexperiencemanager7.1.2/DigitalExperienceManager-
EnterpriseDistribution-7.1.2.1-r54750.3813.jar && \  
wget -P $DOWNLOADS http://central.maven.org/maven2/mysql/mysql-connector-
java/5.1.35/mysql-connector-java-5.1.35.jar  
RUN wget -P $BUNDLES
http://central.maven.org/maven2/org/apache/felix/org.apache.felix.scr/2.0.2/org.apache.felix.scr-2.0.2.jar
&& \  
wget -P $BUNDLES
http://central.maven.org/maven2/org/jbundle/util/osgi/wrapped/org.jbundle.util.osgi.wrapped.org.apache.http.client/4.1.2/org.jbundle.util.osgi.wrapped.org.apache.http.client-4.1.2.jar
&& \  
wget -P $BUNDLES https://store.jahia.com/cms/mavenproxy/private-app-
store/org/jahia/modules/bootstrap3-core/3.4.1/bootstrap3-core-3.4.1.jar && \  
wget -P $BUNDLES https://store.jahia.com/cms/mavenproxy/private-app-
store/org/jahia/modules/bootstrap3-components/3.4.1/bootstrap3-components-3.4.1.jar
&& \  
wget -P $BUNDLES https://store.jahia.com/cms/mavenproxy/private-app-
store/org/jahia/modules/font-awesome/4.6.0/font-awesome-4.6.0.jar && \  
wget -P $BUNDLES https://store.jahia.com/cms/mavenproxy/private-app-
store/org/jahia/modules/distributed-sessions/1.0.0/distributed-
sessions-1.0.0.jar  
COPY ["jahia-install-mysql.xml", "/", "jahia-install-mysql-browsing.xml", "/",
"jahia-install.xml", "/", "distributed-session-filter.xml", "/", "distributed-
session-filter-mapping.xml", "/"]  
ENTRYPOINT ["/bin/sh", "docker-entrypoint.sh"]  
EXPOSE 8080

