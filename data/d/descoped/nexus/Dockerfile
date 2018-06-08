FROM descoped/base  
MAINTAINER Ove Ranheim <oranheim@gmail.com>  
  
# Install Sonatype Nexus  
ENV NEXUS_VERSION 2.14.3-02  
ENV NEXUS_INST /opt/nexus  
ENV SONATYPE_WORK /var/sonatype-work  
ENV IP_ADDRESS 0.0.0.0  
ENV IP_PORT 8081  
ENV UID nexus  
ENV GID sonatype  
ENV LANG C.UTF-8  
ENV CONTEXT_PATH /  
ENV MAX_HEAP 768m  
ENV MIN_HEAP 256m  
ENV JAVA_OPTS -server -Djava.net.preferIPv4Stack=true  
ENV LAUNCHER_CONF ./conf/jetty.xml ./conf/jetty-requestlog.xml  
  
#RUN ["/set-java-home.sh"]  
ADD configure.bash /configure  
ADD nexus.bash /nexus  
RUN chmod +x /configure && chmod +x /nexus  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y createrepo \  
&& apt-get clean autoclean \  
&& apt-get autoremove --yes \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -Lk http://sonatype-
download.global.ssl.fastly.net/nexus/oss/nexus-$NEXUS_VERSION-bundle.tar.gz -o
/root/nexus.tar.gz \  
&& groupadd -r $GID \  
&& useradd -r --create-home --home-dir $NEXUS_INST \--groups $GID \--shell
/bin/bash $UID \  
&& tar zxf /root/nexus.tar.gz --strip=1 -C $NEXUS_INST \  
&& mkdir -p $SONATYPE_WORK  
RUN ["/configure"]  
  
# Launching Nexus  
WORKDIR $NEXUS_INST  
VOLUME $SONATYPE_WORK  
  
COPY entrypoint.bash /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
EXPOSE 8081  
CMD ["/nexus"]  

