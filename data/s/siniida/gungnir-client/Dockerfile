FROM alpine  
MAINTAINER siniida <sinpukyu@gmail.com>  
  
ENV GUNGNIR_VERSION=0.0.1  
RUN apk --no-cache add openjdk8-jre bash \  
&& mkdir /opt \  
&& wget -O - https://s3-ap-northeast-1.amazonaws.com/gennai/release/gungnir-
client-${GUNGNIR_VERSION}-bin.tar.gz | tar zx -C /opt \  
&& chown -R root:root /opt/gungnir-client-${GUNGNIR_VERSION} \  
&& ln -s /opt/gungnir-client-${GUNGNIR_VERSION} /opt/gungnir-client  
  
ENV JAVA_HOME /usr/lib/jvm/default-jvm/jre  
  
WORKDIR /opt/gungnir-client  
  
ADD entry.sh /  
  
ENTRYPOINT ["/entry.sh"]  
CMD ["/opt/gungnir-client/bin/gungnir", "-u root", "-p gennai"]  

