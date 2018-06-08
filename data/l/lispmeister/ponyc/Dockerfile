# build command:  
# 1. make build  
# 2. make test  
# 3. make push  
FROM ubuntu:trusty  
MAINTAINER Markus Fix <lispmeister@gmail.com>  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
ca-certificates \  
clang-3.6 \  
curl \  
git \  
libncurses5-dev \  
libssl-dev \  
llvm-3.6 \  
llvm-3.6-dev \  
make \  
\--no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
  
ENV CC clang-3.6  
ENV CXX clang++-3.6  
RUN mkdir -p /usr/src  
  
RUN curl -SL -o /usr/src/repo.tbz2
ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre2-10.20.tar.bz2 && \  
tar xf /usr/src/repo.tbz2 -C /usr/src && \  
ln -s /usr/src/*pcre* /usr/src/pcre  
  
WORKDIR /usr/src/pcre  
  
RUN ./configure --prefix=/usr && \  
make && \  
make install  
  
# checkout pony project  
WORKDIR /data/pony  
RUN git clone https://github.com/Sendence/ponyc.git  
WORKDIR ponyc  
  
# switch to build tag  
ENV PONY_TAG='sendence-0.1.1'  
RUN git checkout $PONY_TAG  
  
# fix paths  
ENV LD_LIBRARY_PATH="/usr/local/lib:$LD_LIBRARY_PATH"  
# build pony  
RUN make -j4 config=release test && \  
./build/release/ponyc examples/helloworld && \  
./helloworld  
RUN make -j4 test  
RUN make install  
  
# cleanup  
RUN rm -rf /data/pony  
  
# install helper script  
COPY runasuser.sh /root/  
RUN chmod a+x /root/runasuser.sh  
WORKDIR /data  
ENTRYPOINT ["/root/runasuser.sh"]  
  

