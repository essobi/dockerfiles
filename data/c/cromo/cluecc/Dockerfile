FROM debian:wheezy  
MAINTAINER Cristian Romo "cristian.g.romo@gmail.com"  
ENV CLUE_VERSION 0.6  
ENV SPARSE_VERSION 0.4.1  
RUN apt-get update && \  
apt-get install \  
bzip2 \  
curl \  
gcc \  
libgc-dev \  
make \  
patch \  
-y && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /opt  
RUN curl -L -O
http://downloads.sourceforge.net/project/cluecc/clue/clue-$CLUE_VERSION.tar.bz2
&& \  
tar xf clue-$CLUE_VERSION.tar.bz2 && \  
rm clue-$CLUE_VERSION.tar.bz2 && \  
curl -O
http://ftp.be.debian.org/pub/software/devel/sparse/dist/sparse-$SPARSE_VERSION.tar.bz2
&& \  
tar xf sparse-$SPARSE_VERSION.tar.bz2 && \  
rm sparse-$SPARSE_VERSION.tar.bz2 && \  
(cd sparse-$SPARSE_VERSION && \  
patch <../clue-$CLUE_VERSION/sparse.patch && \  
make install) && \  
rm -rf sparse-$SPARSE_VERSION && \  
(mv clue-$CLUE_VERSION clue && \  
cd clue && \  
sed -i 's|/home/dg|/root|' pmfile && \  
./pm)  
  
WORKDIR /source  
CMD ["bash"]

