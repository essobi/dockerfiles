FROM centos  
  
MAINTAINER Utsav Kumar <utsav2307@gmail.com>  
  
RUN mkdir /opt/nexus && \  
cd /opt/nexus && \  
yum install -y wget && \  
yum install -y java && \  
wget http://download.sonatype.com/nexus/3/latest-unix.tar.gz && \  
mv *.tar.gz nexus.tar.gz && \  
tar -xzf nexus.tar.gz && \  
rm -f nexus.tar.gz  
  
RUN chmod -R 777 /opt/nexus  
  
VOLUME ["/opt/nexus/sonatype-work"]  
  
EXPOSE 8081  
RUN cd /opt/nexus/nexus-3.2.1-01/bin/ && chmod +x nexus  
  
WORKDIR /opt/nexus/  
  
ENTRYPOINT ["/bin/bash", "/opt/nexus/nexus-3.2.1-01/bin/nexus", "run"]  
  
CMD ["echo","Nexus started"]  

