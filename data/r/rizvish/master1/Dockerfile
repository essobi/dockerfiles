FROM java:8-jdk  
MAINTAINER strcapstone  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
ENV MAVEN_HOME /opt/maven  
  
ENV KARAF_HOME = /opt/karaf  
ENV KARAF_VERSION = 4.0.8  
ENV POSTGRES_CONTAINER_IP = 172.18.0.2:5432  
ENV MONGO_CONTAINER_IP = 172.18.0.4:27017  
RUN apt-get update \  
&& apt-get -y install maven\  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir /opt/karaf;  
RUN mkdir /tmp/src;  
  
RUN wget http://www-us.apache.org/dist/karaf/${KARAF_VERSION}/apache-
karaf-${KARAF_VERSION}.tar.gz; \  
tar --strip-components=1 -C /opt/karaf -xzf apache-
karaf-${KARAF_VERSION}.tar.gz; \  
rm apache-karaf-${KARAF_VERSION}.tar.gz; \  
mkdir /deploy; \  
sed -i 's/^\\(felix\\.fileinstall\\.dir\s*=\s*\\).*$/\1\/deploy/'
/opt/karaf/etc/org.apache.felix.fileinstall-deploy.cfg  
  
RUN apt-get install -y git  
RUN apt-get clean  
  
WORKDIR /tmp/src/  
  
RUN git clone
https://rizvish:tmp020217@bitbucket.org/strseniordesign/master.git  
  
WORKDIR master  
  
RUN git pull
https://rizvish:tmp020217@bitbucket.org/strseniordesign/master.git  
  
RUN mv /tmp/src/master/"--karafsetup"/karafsetup.script /opt/karaf  
RUN mv /tmp/src/master/"--karafsetup"/org.ops4j.datasource-person.cfg
/opt/karaf/etc  
RUN mv /tmp/src/master/"--karafsetup"/org.ops4j.pax.logging.cfg /opt/karaf/etc  
RUN mv /tmp/src/master/"--karafsetup"/quartz.properties /opt/karaf/etc  
  
RUN mvn clean install; \  
rm -rf /tmp/  
  
WORKDIR /opt/karaf/  
  
RUN bin/start && \  
sleep 100 && \  
bin/client shell:source karafsetup.script && \  
sleep 100  
  
VOLUME ["/deploy"]  
EXPOSE 1099 8101 44444  
ENTRYPOINT ["/opt/karaf/bin/karaf", "start"]  

