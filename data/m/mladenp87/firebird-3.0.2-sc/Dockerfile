FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y wget libtommath0 libicu-dev vim nano
tzdata && \  
cd /root && \  
wget https://sourceforge.net/projects/firebird/files/firebird-linux-
amd64/3.0.2-Release/Firebird-3.0.2.32703-0.amd64.tar.gz/download && \  
tar xzvpf download && cd Firebird* && ./install.sh -silent && \  
echo "ServerMode = SuperClassic" >>/opt/firebird/firebird.conf  
  
ENV PATH $PATH:/opt/firebird/bin  
  
ADD run.sh /opt/firebird/run.sh  
RUN chmod +x /opt/firebird/run.sh  
  
VOLUME /data  
VOLUME /backup  
  
EXPOSE 3050  
ENTRYPOINT ["/opt/firebird/run.sh"]  

