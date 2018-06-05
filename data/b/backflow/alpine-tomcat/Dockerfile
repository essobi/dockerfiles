FROM jeanblanchard/tomcat  
MAINTAINER backflow <hunan_me@163.com>  
  
ENV PATH ${PATH}:/opt/maven/bin  
# install git and maven  
RUN apk --update add git && \  
curl -kLSs http://archive.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz | tar zx -C /opt && \  
rm -rf /var/cache/apk/* && mv /opt/apache-maven-3.3.9 /opt/maven && \  
git clone https://git.oschina.net/backflow/framework.git && \  
cd framework && mvn install && mv target/fw.war /opt/tomcat/webapps/ROOT.war  

