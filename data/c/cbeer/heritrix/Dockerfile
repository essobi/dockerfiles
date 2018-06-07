# HERITRIX  
FROM java  
  
MAINTAINER chris@cbeer.info  
  
ENV HERITRIX_VERSION 3.2.0  
RUN apt-get update && apt-get install -y wget unzip  
  
RUN wget -q -O /tmp/heritrix.tar.gz
http://builds.archive.org/maven2/org/archive/heritrix/heritrix/${HERITRIX_VERSION}/heritrix-${HERITRIX_VERSION}-dist.tar.gz  
RUN tar -C /opt -xzf /tmp/heritrix.tar.gz  
RUN mv /opt/heritrix-${HERITRIX_VERSION} /opt/heritrix  
  
WORKDIR /opt/heritrix  
  
RUN mkdir /mnt/heritrix-data  
  
VOLUME /mnt/heritrix-data  
  
# ADD logging.properties /opt/heritrix/config/logging.properties  
EXPOSE 8443  
ENV FOREGROUND true  
ENTRYPOINT ["/opt/heritrix/bin/heritrix"]  
CMD ["--web-admin heritrix:heritrix", "--web-bind-hosts 0.0.0.0", "--jobs-dir
/mnt/heritrix-data/jobs"]  

