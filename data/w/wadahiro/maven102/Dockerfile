FROM wadahiro/centos-jp:6.8  
LABEL maintainer "Hiroyuki Wada <wadahiro@gmail.com>"  
  
RUN yum install -y java-1.6.0-openjdk java-1.6.0-openjdk-devel && yum install
-y --enablerepo=*debug* java-1.6.0-openjdk-debuginfo && yum install -y git zip
unzip patch && yum clean all  
RUN curl https://archive.apache.org/dist/maven/binaries/maven-1.0.2.tar.gz >
/tmp/maven-1.0.2.tar.gz && tar xzf /tmp/maven-1.0.2.tar.gz -C /usr/share && rm
-f /tmp/maven-1.0.2.tar.gz  
RUN ln -s /usr/share/maven-1.0.2/bin/maven /usr/bin/maven  
  
ENV MAVEN_HOME /usr/share/maven-1.0.2  
ENV JAVA_HOME /usr/lib/jvm/java  
  
  
CMD "/bin/bash"  

