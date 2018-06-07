FROM kitsudo/centos6_jdk8  
MAINTAINER Dave Luo <kitsudo163@163.com>  
  
ENV MAVEN_VERSION=3.3.9  
ENV MAVEN_HOME=/opt/maven  
  
RUN mkdir $MAVEN_HOME && curl -sSL \  
http://archive.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz | \  
tar zxv -C $MAVEN_HOME --strip-components 1  
  
RUN alternatives --install "/usr/bin/mvn" "mvn" "${MAVEN_HOME}/bin/mvn" 1  
  
RUN mkdir ~/.m2 && echo -e '\  
<?xml version="1.0" encoding="UTF-8"?>\n\  
<settings>\n\  
<mirrors>\n\  
<mirror>\n\  
<id>alimaven</id>\n\  
<name>aliyun maven</name>\n\  
<url>http://maven.aliyun.com/nexus/content/groups/public/</url>\n\  
<mirrorOf>central</mirrorOf>\n\  
</mirror>\n\  
</mirrors>\n\  
</settings>\  
' > ~/.m2/settings.xml  
  

