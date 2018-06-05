FROM 99taxis/oracle-java8  
MAINTAINER "Fabio Hisamoto" <fhisamoto@gmail.com>  
  
# Activator  
RUN \  
curl -O http://downloads.typesafe.com/typesafe-activator/1.3.5/typesafe-
activator-1.3.5.zip && \  
unzip typesafe-activator-1.3.5.zip -d / && \  
rm typesafe-activator-1.3.5.zip && \  
chmod a+x activator-dist-1.3.5/activator && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /var/tmp/*  
  
ENV PATH $PATH:/activator-dist-1.3.5  
  
WORKDIR /app  
VOLUME /app

