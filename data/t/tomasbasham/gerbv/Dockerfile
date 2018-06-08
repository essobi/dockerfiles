FROM ubuntu:12.04  
LABEL com.tomasbasham.maintainer "Tomas Basham <me@tomasbasham.co.uk>" \  
com.tomasbasham.version "2.5.0-1" \  
com.tomasbasham.description "gerbv - A Free/Open Source Gerber Viewer"  
  
ENV VERSION 2.5.0-1  
# Install gerbv  
RUN apt-get update \  
&& apt-get install -qy --no-install-recommends gerbv=${VERSION} \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ENTRYPOINT ["/usr/bin/gerbv"]  
CMD ["--help"]  

