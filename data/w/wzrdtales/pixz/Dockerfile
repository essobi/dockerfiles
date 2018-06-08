FROM docker:1.11.1  
  
MAINTAINER Tobias Gurtzick <magic@wizardtales.com>  
  
RUN apk add \--update libarchive asciidoc build-base libarchive-dev git
autoconf automake \  
&& git clone https://github.com/vasi/pixz.git && cd pixz && ./autogen.sh \  
&& ./configure && make && make install && cd .. && rm -Rf pixz \  
&& apk del libarchive-dev asciidoc build-base git autoconf automake \  
&& rm -rf /var/cache/apk/*  
  

