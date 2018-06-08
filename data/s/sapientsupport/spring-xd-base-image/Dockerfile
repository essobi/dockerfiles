FROM java:8  
MAINTAINER Amol  
  
# 'snapshot' or 'release'  
ENV XD_BUILD release  
ENV XD_VERSION 1.3.2.BUILD-SNAPSHOT  
  
RUN groupadd -r springxd && useradd -r -g springxd springxd  
  
RUN wget https://github.com/sapient-support/spring-
xd/releases/download/newVersion/spring-xd-${XD_VERSION}-dist.zip \  
-O /opt/spring-xd-${XD_VERSION}-dist.zip \  
&& unzip /opt/spring-xd-${XD_VERSION}-dist.zip -d /opt/ \  
&& rm /opt/spring-xd-${XD_VERSION}-dist.zip \  
&& apt-get update && apt-get install -y rsync \  
&& /opt/spring-xd-${XD_VERSION}/zookeeper/bin/install-zookeeper \  
&& apt-get autoremove -y rsync \  
&& ln -s /opt/spring-xd-${XD_VERSION} /opt/spring-xd  
  
COPY spring-xd-admin-ui-client-1.3.1.RELEASE.jar /opt/spring-xd/xd/lib/.  
RUN chown -R springxd:springxd /opt/spring-xd-${XD_VERSION}  
  
USER springxd  
WORKDIR /opt/spring-xd  

