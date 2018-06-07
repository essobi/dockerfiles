FROM debian:jessie  
  
MAINTAINER Addis Dittebrandt <addis.dittebrandt@gmail.com>  
  
ENV FACTORIO_VERSION 0.12.33  
ADD md5.txt /opt  
  
RUN apt-get update  
RUN apt-get -y install \  
curl \  
\--no-install-recommends  
RUN apt-get -y clean  
RUN apt-get -y autoclean  
RUN apt-get -y autoremove  
  
WORKDIR /opt  
RUN curl -fsSL -o factorio.tar.gz "http://www.factorio.com/get-
download/${FACTORIO_VERSION}/headless/linux64"  
RUN md5sum --status -c md5.txt  
RUN tar -xzf factorio.tar.gz  
RUN rm factorio.tar.gz  
  
VOLUME /opt/factorio/saves  
EXPOSE 34197/udp  
CMD ["/opt/factorio/bin/x64/factorio", "--start-server", "save"]  

