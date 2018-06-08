FROM openjdk:8-jdk  
MAINTAINER Pojo-ict "info@pojo-ict.nl"  
ENV PKG_LOCATION http://download.sonatype.com/nexus/oss/nexus-latest-
bundle.tar.gz  
ENV TAR_GZ /nexus.tar.gz  
  
ENV RUN_AS_USER root  
RUN apt-get update > /dev/null && \  
mkdir -p /tmp/nexus && \  
curl -Lks ${PKG_LOCATION} -o ${TAR_GZ} && \  
tar xzf ${TAR_GZ} -C /tmp/nexus && \  
mv /tmp/nexus/nex* /nexus && \  
rm -rf ${TAR_GZ} /tmp/nexus  
  
VOLUME ["/sonatype-work"]  
EXPOSE 8081  
CMD ["/nexus/bin/nexus","console"]  

