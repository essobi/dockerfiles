FROM progrium/busybox  
  
MAINTAINER Nitra  
  
WORKDIR /opt/weed  
  
RUN opkg-install curl  
RUN opkg-install wget  
RUN echo "check_certificate = off" >> ~/.wgetrc  
RUN echo tlsv1 >> ~/.curlrc  
  
RUN \  
wget https://bintray.com$(curl -Lk
http://bintray.com/chrislusf/seaweedfs/seaweedfs/_latestVersion | grep
linux_amd64.tar.gz | sed -n "/href/ s/.*href=['\"]\\([^'\"]*\\)['\"].*/\1/gp")
-O - | gunzip | tar -xf - -C /opt/weed/ && \  
mkdir ./bin && mv */* ./bin && \  
chmod +x ./bin/weed  
  
EXPOSE 8080  
EXPOSE 9333  
VOLUME /data  
  
ENV WEED_HOME /opt/weed  
ENV PATH ${PATH}:${WEED_HOME}/bin  
  
ENTRYPOINT ["weed"]  

