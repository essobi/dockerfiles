FROM centos  
  
MAINTAINER Yongyu Lee <aleeyyu@gmail.com>  
  
ENV ACTIVATOR_VERSION 1.2.10  
ENV PATH $PATH:/activator-$ACTIVATOR_VERSION-minimal  
  
RUN \  
yum update -y && \  
yum install -y --nogpgcheck unzip java-1.7.0-openjdk-devel && \  
yum clean all  
  
RUN \  
curl -sOS http://downloads.typesafe.com/typesafe-
activator/$ACTIVATOR_VERSION/typesafe-activator-$ACTIVATOR_VERSION-minimal.zip
&& \  
unzip typesafe-activator-$ACTIVATOR_VERSION-minimal.zip -d / && \  
rm -f typesafe-activator-$ACTIVATOR_VERSION-minimal.zip  
  
VOLUME ["/app"]  
  
WORKDIR /app  
  
EXPOSE 9000  
CMD ["activator", "run"]  

