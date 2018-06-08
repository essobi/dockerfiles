FROM ubuntu:17.10  
RUN apt update && \  
apt install -y software-properties-common && \  
add-apt-repository ppa:visvirial/monacoin && \  
apt update && \  
apt install -y monacoind=0.15.1-artful1  
  
EXPOSE 9401 9402 29000  
VOLUME /root/.monacoin  
  
ENTRYPOINT [ "/usr/bin/monacoind" ]  

