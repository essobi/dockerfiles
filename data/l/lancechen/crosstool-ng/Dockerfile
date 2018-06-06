FROM debian:stable  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update \  
&& apt-get -y install git autoconf gcc g++ gperf bison flex texinfo wget bzip2
help2man gawk libtool-bin ncurses-dev make python-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN git clone https://github.com/crosstool-ng/crosstool-ng \  
&& cd crosstool-ng \  
&& ./bootstrap \  
&& ./configure --prefix=/usr \  
&& make \  
&& make install  
  
RUN useradd -m -s /bin/bash builder  
  
USER builder  
WORKDIR /home/builder  

