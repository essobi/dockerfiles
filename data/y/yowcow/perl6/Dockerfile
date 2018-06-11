FROM ubuntu:trusty  
MAINTAINER yowcow <yowcow@gmail.com>  
  
RUN apt-get -y update && apt-get install -y build-essential curl git && apt-
get clean  
  
RUN cd /tmp && curl -LO http://rakudo.org/downloads/star/rakudo-
star-2016.01.tar.gz \  
&& tar xzf rakudo-star-2016.01.tar.gz \  
&& cd rakudo-star-2016.01 \  
&& perl Configure.pl --gen-moar --prefix /usr/local && make install \  
&& cd /tmp && rm -rf rakudo-star-2016.01 rakudo-star-2016.01.tar.gz  
  
ENV PATH
"/usr/local/share/perl6/site/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"  
RUN panda update && panda install Linenoise  
  
CMD perl6 -v  

