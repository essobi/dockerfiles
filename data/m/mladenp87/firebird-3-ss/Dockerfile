FROM debian:stretch  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y wget libtommath1 libicu-dev vim nano
tzdata procps && \  
ln -sf /usr/lib/x86_64-linux-gnu/libtommath.so.1 /usr/lib/x86_64-linux-
gnu/libtommath.so.0 && \  
cd /root && \  
wget https://sourceforge.net/projects/firebird/files/firebird-linux-
amd64/3.0.2-Release/Firebird-3.0.2.32703-0.amd64.tar.gz/download && \  
tar xzvpf download && cd Firebird* && ./install.sh -silent  
  
ENV PATH $PATH:/opt/firebird/bin  
  
ADD run.sh /opt/firebird/run.sh  
RUN chmod +x /opt/firebird/run.sh  
  
VOLUME /data  
VOLUME /backup  
  
EXPOSE 3050  
ENTRYPOINT ["/opt/firebird/run.sh"]  

