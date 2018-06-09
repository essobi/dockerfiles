FROM alpine  
MAINTAINER siniida <sinpukyu@gmail.com>  
  
ENV STORM_VERSION=0.9.4  
RUN apk --no-cache add openjdk8-jre python \  
&& mkdir /opt \  
&& wget -O - http://ftp.riken.jp/net/apache/storm/apache-
storm-${STORM_VERSION}/apache-storm-${STORM_VERSION}.tar.gz | tar zx -C /opt \  
&& ln -s /opt/apache-storm-${STORM_VERSION} /opt/storm \  
&& mkdir /opt/storm/logs \  
&& chown -R root:root /opt/apache-storm-${STORM_VERSION}  
  
ENV JAVA_HOME /usr/lib/jvm/default-jvm/jre  
  
EXPOSE 6627 6700 6701 6702 6703 8080  
WORKDIR /opt/storm  
  
ADD entry.sh /  
  
ENTRYPOINT ["/entry.sh"]  
CMD ["/opt/storm/bin/storm", "version"]  

