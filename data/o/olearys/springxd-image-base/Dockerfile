FROM java:7  
MAINTAINER Kurt Greiner  
  
ENV XD_VERSION 1.3.0.RELEASE  
  
RUN groupadd -r springxd && useradd -r -g springxd springxd  
  
RUN wget http://repo.spring.io/libs-milestone/org/springframework/xd/spring-
xd/${XD_VERSION}/spring-xd-${XD_VERSION}-dist.zip \  
-O /opt/spring-xd-${XD_VERSION}-dist.zip \  
&& unzip /opt/spring-xd-${XD_VERSION}-dist.zip -d /opt/ \  
&& rm /opt/spring-xd-${XD_VERSION}-dist.zip \  
&& apt-get update && apt-get install -y rsync \  
&& /opt/spring-xd-${XD_VERSION}/zookeeper/bin/install-zookeeper \  
&& chown -R springxd:springxd /opt/spring-xd-${XD_VERSION} \  
&& ln -s /opt/spring-xd-${XD_VERSION} /opt/spring-xd  
  
USER springxd  
WORKDIR /opt/spring-xd  

