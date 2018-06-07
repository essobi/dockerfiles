FROM dockerfile/java  
  
MAINTAINER sistemata  
  
ENV ACTIVATOR_VERSION 1.2.10-minimal  
ENV PATH $PATH:/home/activator-$ACTIVATOR_VERSION  
  
### RUN apt-get install -y unzip java-1.7.0-openjdk-devel && yum clean all  
ADD http://downloads.typesafe.com/typesafe-activator/1.2.10/typesafe-
activator-$ACTIVATOR_VERSION.zip /tmp/activator-$ACTIVATOR_VERSION.zip  
  
RUN cd /home && unzip /tmp/activator-$ACTIVATOR_VERSION.zip && rm -f
/tmp/activator-$ACTIVATOR_VERSION.zip  
  
RUN chmod -R 777 /home/activator-$ACTIVATOR_VERSION  
  
### Clonando App(criando sua pasta) + Dando permissao + entrendo na pasta  
RUN cd /home && git clone https://github.com/emersonjcarvalho/play-docker-
teste.git  
  
RUN chmod -R 777 /home/play-docker-teste  
  
EXPOSE 80 9000  
### CMD cd /home/play-docker-teste && activator start -Dhttp.port=80
-Dhttp.address=0.0.0.0 -J-Xms128M -J-Xmx512m -J-server  
### CMD ["/home/play-docker-teste/activator","run"]  
CMD cd /home/play-docker-teste && activator start -Dhttp.port=80

