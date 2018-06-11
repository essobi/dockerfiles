FROM alpine  
MAINTAINER yowcow <yowcow@gmail.com>  
  
RUN apk update && apk add make gcc libc-dev wget ca-certificates tzdata \  
&& cd /tmp \  
&& wget http://www.cpan.org/src/5.0/perl-5.24.0.tar.gz \  
&& tar xvzf perl-5.24.0.tar.gz \  
&& cd perl-5.24.0 \  
&& ./Configure -des && make && make install \  
&& cd /tmp && rm -rf perl-5.24.0* \  
&& cd /usr/local/bin \  
&& wget https://cpanmin.us/ -O cpanm \  
&& chmod +x cpanm  
  
CMD perl -V && cpanm -V  

