FROM maven:3-jdk-8  
COPY jre/* /usr/lib/jvm/java-1.8-openjdk/jre/lib/security/  
COPY pom.xml /opt/spring-cloud-config-server/  
COPY ks /opt/spring-cloud-config-server/ks  
RUN mkdir /opt/spring-cloud-config-server/target  
COPY jar/* /opt/spring-cloud-config-server/target  
COPY config /config  
RUN keytool -genkeypair -alias mytestkey -keyalg RSA -dname "CN=Web
Server,OU=Unit,O=Organization,L=City,S=State,C=US" -keypass changeme -keystore
/opt/spring-cloud-config-server/ks/server.jks -storepass letmein  
  
RUN mkdir /repo && apt-get update && apt-get install incron less vim -y &&
apt-get clean  
COPY config /config  
COPY repo /repo  
RUN git config --global user.email "root@localhost" && git config --global
user.name "root"  
RUN cd /repo && git init . && git add -A . && git commit -m "First Commit"  
COPY bin /bin  
RUN chmod +x /bin/filesearch.sh  
RUN echo root > /etc/incron.allow  
RUN echo '/repo IN_MODIFY /bin/filesearch.sh' >> /var/spool/incron/root  
  
VOLUME /repo  
  
EXPOSE 8888  
WORKDIR /opt/spring-cloud-config-server/  
#RUN mvn package  
VOLUME /config  
WORKDIR /  
CMD /etc/init.d/incron start && java -Djava.security.egd=file:/dev/./urandom
-jar /opt/spring-cloud-config-server/target/spring-cloud-config-server-*.jar
--server.port=8888 --spring.config.name=application  

