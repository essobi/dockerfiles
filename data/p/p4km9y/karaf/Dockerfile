FROM java:openjdk-8  
MAINTAINER p4km9y  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
ENV KARAF_VERSION 4.0.7  
ENV JAVA_MAX_MEM 256m  
ENV KARAF_EXEC exec  
  
RUN wget http://www-eu.apache.org/dist/karaf/${KARAF_VERSION}/apache-
karaf-${KARAF_VERSION}.tar.gz; \  
mkdir /opt/karaf; \  
tar --strip-components=1 -C /opt/karaf -xzf apache-
karaf-${KARAF_VERSION}.tar.gz; \  
rm apache-karaf-${KARAF_VERSION}.tar.gz; \  
mkdir /opt/deploy; \  
rm -rf /opt/karaf/deploy; \  
ln -s /opt/deploy /opt/karaf/deploy  
  
VOLUME ["/opt/deploy"]  
EXPOSE 1099 8101 44444  
ENTRYPOINT ["/opt/karaf/bin/karaf"]  

