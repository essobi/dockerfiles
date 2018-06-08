FROM ubuntu:16.04  
MAINTAINER pwojda@fromq.com  
  
#install java  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository ppa:webupd8team/java -y  
RUN apt-get update  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java8-installer  
  
#install mule  
RUN wget
https://repository.mulesoft.org/nexus/content/repositories/releases/org/mule/distributions/mule-
standalone/3.8.0/mule-standalone-3.8.0.tar.gz  
RUN echo "ade1c7408dfb6135dedb90fc5b7632f05006fd41 mule-
standalone-3.8.0.tar.gz" | sha1sum -c  
RUN cd /opt && tar xvzf /mule-standalone-3.8.0.tar.gz  
RUN rm /mule-standalone-3.8.0.tar.gz  
RUN ln -s /opt/mule-standalone-3.8.0 /opt/mule  
  
CMD [ "/opt/mule/bin/mule" ]  

