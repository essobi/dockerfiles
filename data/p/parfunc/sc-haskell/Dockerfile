FROM fpco/stack-build:lts-5.16  
  
MAINTAINER Michael Vollmer <mike@recurial.com>  
  
# Note: this needs to change to LLVM 3.7 for GHC 8.0:  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y remove llvm-3.4 libllvm3.4 llvm-3.4-runtime  
RUN apt-get -y update && apt-get -y upgrade && \  
apt-get -y install llvm-3.5 && \  
update-alternatives --install /usr/bin/opt opt /usr/bin/opt-3.5 50 && \  
update-alternatives --install /usr/bin/llc llc /usr/bin/llc-3.5 50  
  
WORKDIR /root  
  
RUN git clone --quiet --recursive git://git.haskell.org/ghc.git  
  
WORKDIR /root/ghc  
  
ENV SUBMOD_SHA 2e98e616dc217b92dd19eeb1f781271e440aad5a  
  
ENV GHC_PREFIX /opt/ghc  
  
# Squish this into one giant command to try to keep the intermediate  
# build data out of the AUFS file system.  
RUN git remote add fork https://github.com/iu-parfunc/ghc.git && \  
git fetch fork && \  
git checkout ${SUBMOD_SHA} && \  
git reset --hard && git clean -dfx && \  
git submodule sync && \  
git submodule update \--init --recursive && \  
mkdir -p ${GHC_PREFIX} && \  
cp mk/build.mk.sample mk/build.mk && \  
./boot && ./configure --quiet --prefix ${GHC_PREFIX} && \  
make -j2 && make install && \  
rm -rf /root/ghc  
  
# Nuke the original copy of GHC 7.10 to avoid confusion:  
RUN rm -rf /opt/stackage/lts-5/ghc  
  
ENV PATH ${GHC_PREFIX}/bin:${PATH}  
WORKDIR /root  

