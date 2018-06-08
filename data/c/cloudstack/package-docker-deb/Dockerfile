FROM ubuntu:16.04  
RUN apt-get -y update  
  
RUN apt-get -y install dpkg-dev devscripts debhelper openjdk-8-jdk genisoimage
python-mysqldb maven python  
  
COPY build.sh /usr/local/bin/build.sh  
  
VOLUME /mnt/build  
  
WORKDIR /mnt/build  
  
CMD ["build.sh"]  

