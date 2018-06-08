FROM debian:jessie  
MAINTAINER Obosob <obosob@riseup.net>  
ENV DEBIAN_FRONTEND noninteractive  
COPY debian-repo.pub /  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
&&\  
apt-key add /debian-repo.pub &&\  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" | tee
/etc/apt/sources.list.d/webupd8team-java.list &&\  
echo "deb http://deb.i2p2.no/ stable main" | tee
/etc/apt/sources.list.d/i2p.list &&\  
apt-get update &&\  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections &&\  
apt-get install --quiet --yes oracle-java7-installer oracle-java7-set-default
i2p procps &&\  
apt-get clean  
RUN sed -i 's/^clientApp\\.0\\.args=/#&/; /^#clientApp.0.args=7657
0\\.0\\.0\\.0 .\/webapps\// s/^#//' /usr/share/i2p/clients.config  
RUN sed -i 's/\\(interface=\\)127\\.0\\.0\\.1/\10.0.0.0/'
/usr/share/i2p/i2ptunnel.config  
RUN sed -i 's/127\\.0\\.0\\.1/0.0.0.0/' /usr/share/i2p/eepsite/jetty*  
WORKDIR /var/lib/i2p  
USER i2psvc  
  
EXPOSE 4444/tcp 4445/tcp 6668/tcp 7657/tcp 7658/tcp  
  
CMD ["/usr/bin/i2prouter", "console"]  

