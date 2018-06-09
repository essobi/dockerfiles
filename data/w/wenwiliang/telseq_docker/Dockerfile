FROM sjackman/linuxbrew-core  
MAINTAINER Wen-Wei Liang <wenwiliang@gmail.com>  
  
USER root  
RUN apt-get update  
RUN apt-get install -y pkg-config autoconf cmake  
  
#Install gcc  
USER linuxbrew  
RUN brew install gcc  
RUN git clone git://github.com/pezmaster31/bamtools.git  
WORKDIR /home/linuxbrew/bamtools  
RUN mkdir builds  
WORKDIR /home/linuxbrew/bamtools/builds  
RUN cmake ..  
RUN make  
  
#Install telseq  
WORKDIR /home/linuxbrew  
RUN git clone https://github.com/zd1/telseq.git  
WORKDIR /home/linuxbrew/telseq/src  
RUN ./autogen.sh  
RUN ./configure --with-bamtools=/home/linuxbrew/bamtools/  
RUN make  
WORKDIR /home/linuxbrew/telseq/src/Telseq/  

