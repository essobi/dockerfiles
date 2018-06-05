FROM ubuntu:14.04  
MAINTAINER Rafael G. Martins <rafael@rafaelmartins.eng.br>  
  
ENV version=0.1.2  
  
RUN apt-get update && apt-get install -y \  
pkg-config gettext zlib1g-dev libffi-dev \  
autoconf automake build-essential libtool libxml2-utils \  
libfcgi-dev shared-mime-info libglib2.0-dev wget peg ca-certificates \  
\--no-install-recommends && apt-get clean  
  
RUN wget
https://github.com/balde/balde/releases/download/v${version}/balde-${version}.tar.xz
&& tar xvf balde-${version}.tar.xz  
  
RUN cd balde-${version} && \  
./autogen.sh && \  
./configure --prefix=/usr && \  
make && \  
make install  

