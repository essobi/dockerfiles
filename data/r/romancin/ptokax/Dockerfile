FROM stackbrew/ubuntu:12.04  
RUN (echo "deb http://archive.ubuntu.com/ubuntu/ precise main restricted
universe multiverse" > /etc/apt/sources.list && echo "deb
http://archive.ubuntu.com/ubuntu/ precise-updates main restricted universe
multiverse" >> /etc/apt/sources.list && echo "deb
http://archive.ubuntu.com/ubuntu/ precise-backports main restricted universe
multiverse" >> /etc/apt/sources.list && echo "deb
http://archive.ubuntu.com/ubuntu/ precise-security main restricted universe
multiverse" >> /etc/apt/sources.list)  
RUN apt-get update  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y g++ make liblua5.1-0-dev
zlib1g-dev wget libtinyxml-dev lua5.1 liblua5.1-filesystem0 liblua5.1-socket2  
  
RUN wget -O /opt/0.5.2.2-nix-src.tgz http://www.ptokax.org/files/0.5.2.2-nix-
src.tgz  
RUN (cd /opt && tar zxvf 0.5.2.2-nix-src.tgz)  
RUN (cd /opt/PtokaX/skein && make)  
RUN (cd /opt/PtokaX/tinyxml && make)  
RUN (cd /opt/PtokaX && make lua51)  
  
ADD run.sh /usr/local/bin/run  
  
EXPOSE 1209  
EXPOSE 411  
WORKDIR /opt/PtokaX  
  
VOLUME /config  
  
CMD ["/usr/local/bin/run"]  

