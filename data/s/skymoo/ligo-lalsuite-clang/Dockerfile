FROM ligo/lalsuite-dev:jessie  
  
LABEL name="LALSuite Clang Development - Debian Jessie" \  
maintainer="Adam Mercer <adam.mercer@ligo.org>" \  
date="20180308" \  
support="Best Effort"  
  
# set version  
ENV VERSION 6.0.0  
ENV PLATFORM x86_64-linux-gnu-debian8  
  
# install wget  
RUN apt-get update && \  
apt-get --assume-yes install wget  
  
# import required key(s)  
RUN gpg --keyserver keys.gnupg.net --recv-key
11E521D646982372EB577A1F8F0871F202119294  
  
# download latest clang build  
RUN wget
http://releases.llvm.org/$VERSION/clang+llvm-$VERSION-$PLATFORM.tar.xz && \  
wget
http://releases.llvm.org/$VERSION/clang+llvm-$VERSION-$PLATFORM.tar.xz.sig  
  
# verify and extract  
RUN gpg --verify clang+llvm-$VERSION-$PLATFORM.tar.xz.sig
clang+llvm-$VERSION-$PLATFORM.tar.xz && \  
tar xf clang+llvm-$VERSION-$PLATFORM.tar.xz && \  
mv clang+llvm-$VERSION-$PLATFORM /opt/clang  
  
# cleanup  
RUN rm clang+llvm-$VERSION-$PLATFORM.tar.xz* && \  
rm -rf /var/lib/apt/lists/*  
  
# add to PATH  
ENV PATH="/opt/clang/bin:${PATH}"  

