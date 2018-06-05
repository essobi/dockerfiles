FROM java:8  
ARG MAVEN_VERSION=3.3.9  
RUN apt-get update && \  
apt-get install -y git ant lsof && \  
mkdir -p /usr/share/maven /usr/share/maven/ref && curl -fsSL
http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz \  
| tar -xzC /usr/share/maven --strip-components=1 && ln -s
/usr/share/maven/bin/mvn /usr/bin/mvn && \  
apt-get clean  
  
RUN mkdir -p /opt/broadleaf && cd /opt/broadleaf && \  
git clone https://github.com/BroadleafCommerce/DemoSite CommunityStarter && \  
cd CommunityStarter && \  
mvn install && \  
mvn spring-boot:build-info  
  
EXPOSE 8082  
EXPOSE 8081  
EXPOSE 8080  
EXPOSE 8443  
EXPOSE 8444  
EXPOSE 8983  
VOLUME /opt/broadleaf  
WORKDIR /opt/broadleaf/CommunityStarter/admin  
CMD ["mvn", "spring-boot:run"]  
  
# CMD ["sh"]  

