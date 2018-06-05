# Version: 0.0.1  
FROM akagelo/debian-jessie-maven3-java-8  
MAINTAINER Oleg Vyukov <gelo@vyukov.ru>  
  
  
#nodejs  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash - && apt-get install
nodejs -y  
  
ADD ./init-settings.xml.sh /init-settings.xml.sh  

