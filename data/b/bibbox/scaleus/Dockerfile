# Scaleus Container  
#  
# VERSION 0.0.1  
#  
# https://github.com/bioinformatics-ua/scaleus  
FROM java:8  
MAINTAINER Robert Reihs <robert.reihs@gmail.com>  
  
RUN apt-get update \  
&& apt-get -y install wget \  
&& mkdir /opt/scaleus \  
&& wget https://github.com/bioinformatics-
ua/scaleus/releases/download/1.2/scaleus-1.0-jar-with-dependencies.jar -O
/opt/scaleus/scaleus-1.0-jar-with-dependencies.jar  
  
ADD scripts /opt/scripts  
WORKDIR /opt/scripts  
RUN chmod a+x *.sh  
  
ENTRYPOINT ["/opt/scripts/entrypoint.sh"]

