FROM ubuntu:latest  
  
ARG URBIT_VERSION=0.4.3  
ENV URBIT_VERSION=${URBIT_VERSION}  
  
LABEL maintainer="<rubyisbeautiful> bcptaylor@gmail.com"  
  
RUN apt-get update -y && apt-get install -y \  
autoconf \  
automake \  
cmake \  
curl \  
exuberant-ctags \  
g++ \  
libgmp3-dev \  
libcurl4-gnutls-dev \  
libncurses5-dev \  
libsigsegv-dev \  
libssl-dev \  
libtool \  
make \  
openssl \  
ragel \  
re2c \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /urbit  
  
WORKDIR /urbit  
  
RUN curl -o urbit-$URBIT_VERSION.tar.gz
https://media.urbit.org/dist/src/urbit-$URBIT_VERSION.tar.gz \  
&& tar xzf urbit-$URBIT_VERSION.tar.gz \  
&& rm -f urbit-$URBIT_VERSION.tar.gz  
  
WORKDIR /urbit/urbit-$URBIT_VERSION  
  
RUN make  
  
RUN curl -o urbit.pill https://bootstrap.urbit.org/latest.pill  

