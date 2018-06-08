FROM ubuntu:14.04  
MAINTAINER David Dunwoody <david.dunwoody@gmail.com>  
RUN apt-get update && apt-get install -y ant build-essential git software-
properties-common  
RUN add-apt-repository ppa:webupd8team/java  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get update && apt-get install -y oracle-java8-installer oracle-
java8-set-default  
WORKDIR /tmp  
RUN git clone git://github.com/cryptobiu/scapi.git  
WORKDIR /tmp/scapi  
RUN git submodule init && git submodule update  
RUN make && make install prefix=/usr  
WORKDIR /root  
RUN rm -rf /tmp/scapi  

