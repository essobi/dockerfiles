FROM openjdk:8  
RUN apt-get update && apt-get install -y ant exuberant-ctags tomcat7 unzip  
  
RUN mkdir /tmp/opengrok  
  
RUN wget
https://github.com/OpenGrok/OpenGrok/files/467358/opengrok-0.12.1.6.tar.gz.zip
-O /tmp/opengrok.tar.gz.zip  
RUN wget http://jflex.de/release/jflex-1.6.1.tar.gz -O /tmp/jflex.tar.gz  
  
RUN unzip /tmp/opengrok.tar.gz.zip -d /tmp/  
RUN tar xzvf /tmp/opengrok-0.12.1.6.tar.gz -C /tmp/opengrok  
RUN tar xzvf /tmp/jflex.tar.gz -C /tmp/opengrok  
RUN cp /tmp/opengrok/jflex-1.6.1/lib/jflex-1.6.1.jar
/tmp/opengrok/opengrok-0.12.1.6/lib/  
RUN cp -Rap /tmp/opengrok/opengrok-0.12.1.6/bin /usr/local/  
RUN cp -Rap /tmp/opengrok/opengrok-0.12.1.6/lib /usr/local/  
  
RUN mkdir /var/opengrok  
RUN mkdir /var/opengrok/etc  
RUN mkdir /var/opengrok/data  
RUN mkdir /var/opengrok/src  
  
RUN OpenGrok deploy  
RUN OpenGrok index  
  
EXPOSE 8080  
CMD /etc/init.d/tomcat7 restart ; /bin/bash  
  

