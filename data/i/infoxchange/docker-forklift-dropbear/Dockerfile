# Conservative libc  
FROM debian:squeeze  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -qq install bzip2 gcc make patch zlib1g-dev  
  
ADD https://matt.ucc.asn.au/dropbear/releases/dropbear-2014.63.tar.bz2 \  
/dropbear.tar.bz2  
  
RUN tar xf dropbear.tar.bz2  
RUN mv dropbear-* dropbear  
  
WORKDIR /dropbear  
  
ADD https://github.com/koterpillar/dropbear/compare/environment.patch \  
/dropbear/environment.patch  
  
RUN patch -p1 < environment.patch  
  
RUN ./configure  
RUN make PROGRAMS=dropbear  
  
ENTRYPOINT ["cat", "/dropbear/dropbear"]  

