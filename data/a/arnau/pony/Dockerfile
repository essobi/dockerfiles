FROM debian:sid  
MAINTAINER Arnau Siches <asiches@gmail.com>  
  
ENV PONY_VERSION 0.1.7  
ENV PONY_SRC_DIR /usr/local/ponyc  
  
RUN apt-get update -qqy \  
&& apt-get install -qqy \  
build-essential \  
curl \  
libncurses-dev \  
libnuma-dev \  
llvm-3.6-dev \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -s -SL
"https://github.com/CausalityLtd/ponyc/archive/$PONY_VERSION.tar.gz" \  
| tar -xzf - \  
&& mv /ponyc-$PONY_VERSION $PONY_SRC_DIR  
  
WORKDIR $PONY_SRC_DIR  
  
RUN make config=release  
ENV PATH $PATH:$PONY_SRC_DIR/build/release  
  
CMD ["make", "test"]  

