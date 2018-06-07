FROM ubuntu:trusty  
  
MAINTAINER Thomas Spellman <thos37@gmail.com>  
  
# Add a repo where OpenJDK can be found.  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update  
  
# Auto-accept the Oracle JDK license  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y oracle-java8-installer  
RUN apt-get install -y unzip curl  
  
ENV DATOMIC_VERSION 0.9.5327  
ENV HOST 0.0.0.0  
ENV ALT_HOST datomic-free  
  
# using curl seems to work better with docker build caching  
#ADD https://my.datomic.com/downloads/free/${DATOMIC_VERSION} /tmp/datomic.zip  
RUN curl -L -o /tmp/datomic.zip
https://my.datomic.com/downloads/free/${DATOMIC_VERSION}  
  
RUN unzip /tmp/datomic.zip  
RUN rm /tmp/datomic.zip  
  
WORKDIR datomic-free-${DATOMIC_VERSION}  
  
RUN cp config/samples/free-transactor-template.properties
transactor.properties  
  
# for docker, listen on all interfaces  
RUN sed "s/host=localhost/host=${HOST}/" -i transactor.properties  
  
# also listen on the docker-created link host name  
RUN sed "/host=${HOST}/a alt-host=${ALT_HOST}" -i transactor.properties  
  
# smaller to run better on small virtual machines  
RUN sed "s/memory-index-max=256m/memory-index-max=128m/" -i
transactor.properties  
  
RUN mkdir /data  
RUN sed "s/# data-dir=data/data-dir=\/data/" -i transactor.properties  
VOLUME /data  
  
RUN mkdir /log  
RUN sed "s/# log-dir=log/log-dir=\/log/" -i transactor.properties  
VOLUME /log  
  
ADD start.sh ./  
RUN chmod +x start.sh  
  
EXPOSE 4334 4335 4336  
ENV XMX=512m XMS=256m  
  
CMD ["./start.sh"]  

