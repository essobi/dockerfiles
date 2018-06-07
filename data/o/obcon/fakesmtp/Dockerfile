FROM obcon/java  
  
MAINTAINER http://obcon.de Marco Obermeyer <marco.obermeyer@obcon.de>  
  
RUN mkdir /opt/fakesmtp && cd /opt/fakesmtp && wget
http://nilhcem.github.com/FakeSMTP/downloads/fakeSMTP-latest.zip && unzip
fakeSMTP-latest.zip && rm fakeSMTP-latest.zip  
  
RUN mkdir /opt/jibble && cd /opt/jibble && wget
http://www.jibble.org/files/WebServerLite.jar  
  
RUN mkdir /var/log/fakesmtp  
  
RUN mkdir -p /etc/service/fakesmtp  
RUN echo "#!/bin/bash" > /etc/service/fakesmtp/run  
RUN echo "java -jar /opt/fakesmtp/fakeSMTP-1.13.jar -o /var/log/fakesmtp -s -b
-p 25" >> /etc/service/fakesmtp/run  
RUN chmod +x /etc/service/fakesmtp/run  
  
RUN mkdir -p /etc/service/jibble  
RUN echo "#!/bin/bash" > /etc/service/jibble/run  
RUN echo "java -jar /opt/jibble/WebServerLite.jar /var/log/fakesmtp 80" >>
/etc/service/jibble/run  
RUN chmod +x /etc/service/jibble/run  
  
EXPOSE 25 80  
CMD ["/sbin/my_init"]  

