FROM alpine:latest  
  
LABEL maintainer="docker@shadowhunt.de"  
  
RUN apk \--update upgrade \  
&& apk add bash curl g++ make unzip \  
&& curl \--location \--output /tmp/litmus-master.zip
https://github.com/thrawn-sh/litmus/archive/master.zip \  
&& ls -l /tmp/litmus-master.zip \  
&& cd /tmp \  
&& unzip litmus-master.zip \  
&& cd litmus-master \  
&& ./configure \--silent \--prefix=/usr \  
&& make \  
&& make install \  
&& cd / \  
&& rm -f -r /tmp/litmus-master.zip /tmp/litmus-master \  
&& apk del bash curl g++ make unzip \  
&& rm -f -r /var/cache/apk/*  
  
ENTRYPOINT ["/usr/bin/litmus"]  
CMD []  

