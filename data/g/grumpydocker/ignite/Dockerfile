FROM java:8-jdk  
MAINTAINER Alex Sherwin <alex.sherwin@gmail.com>  
ENTRYPOINT ["/ignite/bin/ignite.sh"]  
  
ENV IGNITE_VERSION 1.1.0-incubating  
  
RUN apt-get update && apt-get install -y vim wget ca-certificates && rm -rf
/var/lib/apt/lists/* && \  
wget http://mirror.symnds.com/software/Apache//incubator/ignite/1.1.0/apache-
ignite-fabric-${IGNITE_VERSION}-bin.zip -O /temp.zip && \  
unzip /temp.zip && mv /apache-ignite-fabric-${IGNITE_VERSION}-bin /ignite &&
rm /temp.zip && \  
apt-get -y purge --auto-remove wget  
  
WORKDIR /ignite  
  
EXPOSE 47100 48100

