FROM ubuntu:trusty  
MAINTAINER yowcow <yowcow@gmail.com>  
  
RUN apt-get -y update && apt-get install -y build-essential curl && apt-get
clean  
  
RUN cd /tmp && curl -LO http://www.cpan.org/src/5.0/perl-5.16.3.tar.gz \  
&& tar xvzf perl-5.16.3.tar.gz \  
&& cd perl-5.16.3 \  
&& ./Configure -des && make && make install \  
&& cd /tmp && rm -rf perl-5.16.3.tar.gz perl-5.16.3 \  
&& cd /usr/local/bin && curl -L https://cpanmin.us/ -o cpanm && chmod +x cpanm  
  
CMD perl -V && cpanm -V  

