FROM pilchard/centos  
MAINTAINER pilchard <ludundun@126.com>  
  
LABEL Description="Java + CentOS (OpenJDK)"  
  
ARG JAVA_VERSION=8  
ARG JAVA_RELEASE=JDK  
  
ENV JAVA_HOME=/usr  
  
RUN \  
pkg="java-1.$JAVA_VERSION.0-openjdk"; \  
if [ "$JAVA_RELEASE" = "JDK" ]; then \  
pkg="$pkg-devel"; \  
else \  
pkg="$pkg-headless"; \  
fi; \  
yum install -y "$pkg" && \  
yum clean all  
  
CMD /bin/bash  

