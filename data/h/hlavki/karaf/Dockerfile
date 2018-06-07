FROM openjdk:8  
MAINTAINER Michal Hlavac <miso@hlavki.eu>  
  
ENV KARAF_USER karaf  
ENV KARAF_UID 8181  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
ENV KARAF_VERSION 4.1.2  
ENV JAVA_MAX_MEM 256m  
ENV KARAF_EXEC exec  
  
RUN groupadd -r $KARAF_USER \--gid=$KARAF_UID && useradd -rm -g $KARAF_USER
\--uid=$KARAF_UID $KARAF_USER  
  
RUN wget http://www-eu.apache.org/dist/karaf/${KARAF_VERSION}/apache-
karaf-${KARAF_VERSION}.tar.gz; \  
mkdir -p /opt/karaf; \  
tar --strip-components=1 -C /opt/karaf -xzf apache-
karaf-${KARAF_VERSION}.tar.gz; \  
rm apache-karaf-${KARAF_VERSION}.tar.gz  
  
RUN sed -i 's/log4j\\.rootLogger=INFO,\ out,\
osgi\:\\*/log4j\\.rootLogger=INFO,\ out,\ stdout,\ osgi\:\\*/'
/opt/karaf/etc/org.ops4j.pax.logging.cfg  
  
# Add default maven repository  
RUN echo org.ops4j.pax.url.mvn.defaultRepositories =
file:///opt/maven/repository@id=local.app@snapshots >>
/opt/karaf/etc/org.ops4j.pax.url.mvn.cfg  
  
# Prepare data directory  
RUN mkdir -p /opt/karaf/data /opt/karaf/data/log \  
&& chown -R $KARAF_USER.$KARAF_USER /opt/karaf \  
&& chmod 700 /opt/karaf/data  
  
EXPOSE 1099 8101 44444  
USER $KARAF_USER  
  
CMD ["/opt/karaf/bin/karaf", "run"]  

