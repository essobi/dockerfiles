## Dockerfile for a haskell environment in CentOS 6  
FROM centos:6  
MAINTAINER Dmitrij Koniajev <dimchansky@gmail.com>  
  
## Install dependencies  
RUN yum install -y \  
gcc \  
gmp-devel \  
pcre-devel \  
perl \  
tar \  
which \  
xz \  
zlib-devel \  
&& yum clean all --releasever=6 \  
&& ln -s /lib64/libtinfo.so.5 /lib64/libtinfo.so  
  
## set ghc and tools versions  
ENV GHC_VERSION=7.8.4 \  
CABAL_VERSION=1.22.2.0 \  
ALEX_VERSION=3.1.4 \  
HAPPY_VERSION=1.19.5 \  
C2HS_VERSION=0.25.1  
## Download and install GHC  
RUN curl -s
"https://downloads.haskell.org/~ghc/${GHC_VERSION}/ghc-${GHC_VERSION}-x86_64-unknown-
linux-centos65.tar.xz" > /tmp/ghc.tar.xz \  
&& tar xf /tmp/ghc.tar.xz -C /tmp \  
&& cd /tmp/ghc-${GHC_VERSION} && ./configure --prefix /opt/ghc/${GHC_VERSION}
\  
&& make install \  
&& cd /tmp && rm -rf /tmp/* && rm -rf /root/{*,.??*}  
  
## set PATH for GHC  
ENV PATH /opt/ghc/${GHC_VERSION}/bin:$PATH  
  
## Donwload and install Cabal/Cabal-Install  
RUN curl -s "https://www.haskell.org/cabal/release/cabal-
install-${CABAL_VERSION}/cabal-install-${CABAL_VERSION}.tar.gz" >
/tmp/cabal.tar.gz \  
&& tar xf /tmp/cabal.tar.gz -C /tmp \  
&& cd /tmp/cabal-install-${CABAL_VERSION} \  
&& PREFIX=/opt/cabal/${CABAL_VERSION} ./bootstrap.sh \  
&& rm -rf /opt/cabal/${CABAL_VERSION}/lib \  
&& cd /tmp && rm -rf /tmp/* && rm -rf /root/{*,.??*}  
  
## set PATH for cabal  
ENV PATH /opt/cabal/${CABAL_VERSION}/bin:$PATH  
  
## Install Cabal to match cabal-install  
## Install common Haskell build tools  
RUN cabal update \  
&& cabal install Cabal-${CABAL_VERSION} \  
\--global \  
\--enable-library-profiling \  
\--prefix=/opt/ghc/${GHC_VERSION} \  
\--libsubdir=\$compiler/\$pkgkey \  
\--datasubdir=\$compiler/\$pkgkey \  
\--docdir=\$datadir/doc/ghc/html/libraries \  
\--htmldir=\$datadir/doc/ghc/html/libraries \  
&& cabal install alex-${ALEX_VERSION} --prefix=/opt/alex/${ALEX_VERSION} && rm
-rf /opt/alex/${ALEX_VERSION}/lib \  
&& cabal install happy-${HAPPY_VERSION} --prefix=/opt/happy/${HAPPY_VERSION}
&& rm -rf /opt/happy/${HAPPY_VERSION}/lib \  
&& PATH=/opt/alex/${ALEX_VERSION}/bin/:/opt/happy/${HAPPY_VERSION}/bin/:$PATH
cabal install c2hs-${C2HS_VERSION} --prefix=/opt/c2hs/${C2HS_VERSION} && rm
-rf /opt/c2hs/${C2HS_VERSION}/lib \  
&& rm -rf /root/{*,.??*}  
  
## set PATH for tools  
ENV PATH
/opt/alex/${ALEX_VERSION}/bin/:/opt/happy/${HAPPY_VERSION}/bin/:/opt/c2hs/${C2HS_VERSION}/bin/:$PATH  
  
## run ghci by default unless a command is specified  
CMD ["ghci"]  

