FROM ubuntu:14.04  
MAINTAINER Chris Daish <chrisdaish@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get install --no-install-recommends -y wget \  
libc6:i386 \  
libstdc++6:i386 \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV GEEKBENCHVERSION Geekbench-3.4.1-Linux  
ENV GEEKBENCHPACKAGE $GEEKBENCHVERSION.tar.gz  
  
RUN wget --quiet --no-check-certificate
http://cdn.primatelabs.com/$GEEKBENCHPACKAGE -O /tmp/$GEEKBENCHPACKAGE \  
&& mkdir -p /opt/geekbench \  
&& tar xzf /tmp/$GEEKBENCHPACKAGE -C /opt/geekbench \  
&& rm -rf /tmp/$GEEKBENCHPACKAGE  
  
CMD ["/opt/geekbench/dist/Geekbench-3.4.1-Linux/geekbench"]  

