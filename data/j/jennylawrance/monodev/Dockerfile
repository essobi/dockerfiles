FROM ubuntu:16.04  
RUN apt-get update  
RUN apt-get install -y apache2 apache2-dev  
RUN apt-get install -y autoconf  
RUN apt-get install -y libtool-bin  
RUN apt-get install -y automake  
RUN apt-get install -y build-essential  
RUN apt-get install -y gettext  
RUN apt-get install -y cmake  
RUN apt-get install -y vim  
RUN apt-get install -y git-core  
RUN apt-get install -y tzdata  
RUN apt-get install -y pkg-config  
  
RUN mkdir /home/src  
  
WORKDIR /home/src  
  
RUN git clone https://github.com/mono/mod_mono.git  
  
RUN git clone https://github.com/JennyLawrance/mono.git  
  
RUN git clone https://github.com/mono/xsp.git  
  
WORKDIR /home/src/mod_mono  
  
RUN ./autogen.sh --sysconfdir=/etc  
RUN make  
RUN make install  
  
WORKDIR /home/src/mono  
  
RUN ./autogen.sh --sysconfdir=/etc  
RUN make  
RUN make install  
  
WORKDIR /home/src/xsp  
  
RUN ./autogen.sh --sysconfdir=/etc  
RUN make  
RUN make install

