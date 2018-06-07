FROM alpine  
MAINTAINER siniida <sinpukyu@gmail.com>  
  
ENV GUNGNIR_VERSION=0.0.1  
RUN apk --no-cache add openjdk8-jre bash \  
&& mkdir /opt \  
&& wget -O - https://s3-ap-northeast-1.amazonaws.com/gennai/release/gungnir-
server-${GUNGNIR_VERSION}-bin.tar.gz | tar zx -C /opt \  
&& ln -s /opt/gungnir-server-${GUNGNIR_VERSION} /opt/gungnir-server \  
&& mkdir -p /opt/gungnir-server/logs \  
&& chown -R root:root /opt/gungnir-server-${GUNGNIR_VERSION}  
  
ENV JAVA_HOME /usr/lib/jvm/default-jvm/jre  
  
EXPOSE 7100 7200 7300  
WORKDIR /opt/gungnir-server  
  
ADD entry.sh /  
  
ENTRYPOINT ["/entry.sh"]  

