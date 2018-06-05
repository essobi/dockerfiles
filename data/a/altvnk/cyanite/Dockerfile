FROM debian:wheezy  
MAINTAINER Alexander Litvinenko <altvnk@me.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
COPY files/etc/apt/sources.list.d/ /etc/apt/sources.list.d/  
  
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys F758CE318D77295D && \  
apt-key adv --keyserver pgp.mit.edu --recv-keys 2B5C1B00 && \  
apt-key adv --keyserver pgp.mit.edu --recv-keys 0353B12C && \  
apt-key adv --keyserver pgp.mit.edu --recv-keys EEA14886  
  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
  
RUN apt-get update && apt-get -qq -y install cassandra oracle-java8-installer
oracle-java8-set-default && apt-get clean && rm -rf /var/cache/apt  
  
COPY files/opt/cyanite/ /opt/cyanite/  
  
COPY files/etc/cyanite.yaml /etc/cyanite.yaml  
  
EXPOSE 2003 2003 8080  
CMD [ "/opt/cyanite/cyanite.sh" ]  

