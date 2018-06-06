FROM java:8-jdk  
  
MAINTAINER cloud57  
  
ENV KARAF_VERSION=4.1.1  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
ENV KARAF_VERSION=4.1.1  
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.0/dumb-init_1.2.0_amd64; \  
chmod +x /usr/local/bin/dumb-init; \  
wget http://www-us.apache.org/dist/karaf/${KARAF_VERSION}/apache-
karaf-${KARAF_VERSION}.tar.gz; \  
mkdir /opt/karaf; \  
tar --strip-components=1 -C /opt/karaf -xzf apache-
karaf-${KARAF_VERSION}.tar.gz; \  
rm apache-karaf-${KARAF_VERSION}.tar.gz;  
  
EXPOSE 1099 8101 44444  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]  
  
CMD ["/opt/karaf/bin/karaf"]  

