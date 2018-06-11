FROM wolfitem/baseimage:desktop  
MAINTAINER wolfitem <wei.wu86@hotmail.com>  
USER root  
  
RUN apt-get update  
  
RUN curl 'http://download-cf.jetbrains.com/webide/PhpStorm-8.0.3.tar.gz' >
/tmp/PhpStorm.tar.gz && cd /opt && tar -zxvf /tmp/PhpStorm.tar.gz && rm
/tmp/PhpStorm.tar.gz  
  
# Install prerequisites  
RUN apt-get install -y openjdk-7-jdk lib32z1 lib32ncurses5 lib32bz2-1.0
lib32stdc++6  
  
#clean up  
RUN apt-get clean  
RUN apt-get purge  
  
#USER developer  
CMD /opt/PhpStorm-139.1348/bin/phpstorm.sh  

