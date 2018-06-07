FROM ubuntu:14.04  
MAINTAINER Study Hsueh <ph.study@gmail.com>  
  
RUN apt-get update -q && apt-get install -qy ant openjdk-7-jdk mysql-client  
  
ADD . /en  
WORKDIR /en  
  
RUN ant  
  
RUN chmod +x serverstart.sh  
  
RUN tar jxf /en/maps/maps.tar.bz2 -C /en/maps/ && rm /en/maps/maps.tar.bz2  
  
ADD ./docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 2000/tcp  
  
CMD ["/en/serverstart.sh"]  

