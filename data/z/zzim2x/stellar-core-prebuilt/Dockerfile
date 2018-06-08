FROM zzim2x/ubuntu-dev:14.04-gcc5  
  
RUN mkdir -p /opt/src  
RUN apt install -y pandoc  
  
ENV STELLAR_VERSION 13d55680  
  
RUN cd /opt/src && git clone https://github.com/stellar/stellar-core  
RUN cd /opt/src/stellar-core && git checkout $STELLAR_VERSION && git submodule
init && git submodule update  
  
WORKDIR /opt/src/stellar-core  
  
RUN ./autogen.sh  
RUN CXX=g++-5 ./configure  
RUN make  
RUN make install  
  

