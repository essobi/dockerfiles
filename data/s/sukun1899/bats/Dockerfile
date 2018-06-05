FROM ubuntu:xenial  
MAINTAINER su-kun1899 <higedrum.coz@gmail.com>  
  
RUN apt-get update \  
&& apt-get -y upgrade  
  
# install for ci  
RUN apt-get -y install git \  
&& apt-get -y install ssh \  
&& apt-get -y install tar \  
&& apt-get -y install gzip \  
&& apt-get -y install ca-certificates  
  
# install bats  
RUN apt-get install -y software-properties-common \  
&& add-apt-repository -y ppa:duggan/bats \  
&& apt-get -y install bats  
  
# install for sample project  
RUN apt-get -y install curl  
  
CMD tail -f /dev/null  

