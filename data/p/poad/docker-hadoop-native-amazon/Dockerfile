FROM poad/docker-java-amazon:2017.03  
MAINTAINER Kenji Saito  
  
USER root  
  
RUN yum groupinstall "Development Tools" -y  
RUN yum install -y cmake zlib-devel openssl-devel \  
cmake zlib-devel openssl-devel protobuf protobuf-devel  
  
# hadoop  
RUN curl -s
https://archive.apache.org/dist/hadoop/common/hadoop-2.7.3/hadoop-2.7.3-src.tar.gz
| tar -xz -C /tmp  
RUN cd /tmp  
  
RUN curl -sL
https://archive.apache.org/dist/maven/maven-3/3.5.2/binaries/apache-
maven-3.5.2-bin.tar.gz | tar -xz -C /usr/local/  
RUN cd /usr/local && ln -s ./apache-maven-3.5.2 maven  
  
ENV PATH ${PATH}:/usr/local/maven/bin  
ENV JAVA_HOME /usr/lib/jvm/java  
ENV PATH ${JAVA_HOME}:${PATH}  
  
WORKDIR /tmp/hadoop-2.7.3-src/  
RUN mvn package -Pdist,native -DskipTests -Dmaven.javadoc.skip=true -Dtar  
  
# tar to stdout  
CMD cd /tmp/hadoop-2.7.3-src/hadoop-dist/target/hadoop-2.7.3/lib && \  
tar czf /root/hadoop-native.tar.gz native  
  

