FROM ubuntu:14.04  
ENV ERLANG_VSN R16B03  
  
RUN apt-get update && \  
apt-get install -y curl \  
build-essential \  
libncurses5-dev \  
libssl-dev \  
unixodbc-dev  
  
RUN curl -O https://raw.githubusercontent.com/yrashk/kerl/master/kerl && \  
chmod a+x kerl && \  
./kerl build ${ERLANG_VSN} ${ERLANG_VSN} && \  
./kerl install ${ERLANG_VSN} /opt/erlang  
  
ENV PATH /opt/erlang/bin:$PATH  

