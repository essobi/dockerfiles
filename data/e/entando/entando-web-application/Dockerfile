FROM centos:7  
MAINTAINER p.masala@entando.com  
USER root  
RUN useradd -ms /bin/bash entando  
ENV JAVA_HOME /opt/jdk1.8.0_141  
ENV JRE_HOME /opt/jdk1.8.0_141/jre  
ENV MAVEN_HOME /usr/share/maven  
  
  
RUN yum install -y curl maven imagemagick wget \  
&& cd /opt \  
&& wget --no-cookies --no-check-certificate --header \  
"Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-
securebackup-cookie" \  
"http://download.oracle.com/otn-
pub/java/jdk/8u141-b15/336fa29ff2bb4ef291e347e091f7f4a7/jdk-8u141-linux-x64.tar.gz"
\  
&& tar xzf jdk-8u141-linux-x64.tar.gz \  
&& rm -f jdk-8u141-linux-x64.tar.gz \  
&& rm -f /usr/bin/java /usr/bin/jar /usr/bin/javac \  
&& cd jdk1.8.0_141/ \  
&& ln -s /opt/jdk1.8.0_141/bin/java /usr/bin/java \  
&& ln -s /opt/jdk1.8.0_141/bin/jar /usr/bin/jar \  
&& ln -s /opt/jdk1.8.0_141/bin/javac /usr/bin/javac \  
&& yum clean all -y  
USER entando  
RUN cd /home/entando \  
&& mvn archetype:generate -B \  
-Dfilter=entando \  
-DarchetypeGroupId=org.entando.entando \  
-DarchetypeArtifactId=entando-archetype-portal-generic \  
-DgroupId=org.entando \  
-DartifactId=web \  
-Dversion=1.0-SNAPSHOT \  
-Dpackage=org.entando  
  
WORKDIR /home/entando/web  
  
CMD ["mvn", "clean", "install", "-DskipTests", "jetty:run"]  
EXPOSE 8080  

