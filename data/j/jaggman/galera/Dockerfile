FROM ubuntu:xenial  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV container docker  
  
RUN apt-get update \  
&& apt-get install -y software-properties-common \  
&& apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xF1656F24C74CD1D8 \  
&& add-apt-repository 'deb http://ftp.osuosl.org/pub/mariadb/repo/10.1/ubuntu
xenial main' \  
&& apt-get update \  
&& apt-get install -y mariadb-server \  
&& apt-get install -y vim \  
&& apt-get clean  
  
EXPOSE 3306 4567 4568 4444  
VOLUME [ "/var/lib/mysql" ]  
  
COPY run.sh /  
  
CMD /run.sh  
  

