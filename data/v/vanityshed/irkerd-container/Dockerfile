FROM alpine:3.6  
MAINTAINER Stevesbrain  
RUN set -x \  
&& apk add \--no-cache make asciidoc python-dev python2 xmlto git \  
&& git clone https://gitlab.com/esr/irker.git \  
&& cd irker \  
&& make \  
&& make install \  
&& apk del git make asciidoc python-dev xmlto  
  
ENTRYPOINT ["/usr/bin/irkerd"]  

