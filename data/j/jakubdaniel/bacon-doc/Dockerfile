FROM ubuntu:xenial  
MAINTAINER Jakub Daniel  
  
# system dependencies  
RUN apt-get -y update  
RUN apt-get -y install cabal-install ghc git mercurial make llvm clang g++
zlib1g-dev vim  
#RUN apt-get -y install libgtk-3-dev  
# user  
RUN useradd -m bacon  
  
USER bacon  
CMD cd && bash  
  
ENV PATH ${PATH}:/home/bacon/.cabal/bin  
  
# haskell dependencies  
RUN cabal update  
#RUN cabal install alex happy  
#RUN cabal install gtk2hs-buildtools  
# third party dependencies  
RUN cd /home/bacon && git clone https://github.com/Z3Prover/z3  
  
RUN cd /home/bacon/z3 \  
&& git checkout tags/z3-4.4.1 \  
&& ./configure --prefix=/usr \  
&& cd build \  
&& make  
  
USER root  
  
RUN cd /home/bacon/z3/build && make install  
  
USER bacon  
  
# up-to-date / bleeding edge dependencies  
RUN cd /home/bacon && hg clone https://bitbucket.org/jd823592/z3-haskell  
  
# non-haskell  
RUN cd /home/bacon && git clone https://github.com/d3sformal/bacon-
preprocessor  
  
RUN cd /home/bacon/bacon-preprocessor && make  
# haskell  
RUN cd /home/bacon && git clone https://github.com/d3sformal/bacon-core  
RUN cd /home/bacon && git clone https://github.com/d3sformal/bacon-doc  
#RUN cd /home/bacon && git clone https://github.com/d3sformal/bacon-gui  
RUN cd /home/bacon && git clone https://github.com/d3sformal/bacon-main  
  
RUN cd /home/bacon/bacon-core \  
&& cabal sandbox init \  
&& cabal sandbox add-source ../z3-haskell  
#RUN cd /home/bacon/bacon-gui \  
# && cabal sandbox init \  
# && cabal sandbox add-source ../z3-haskell \  
# && cabal sandbox add-source ../bacon-core  
RUN cd /home/bacon/bacon-main \  
&& cabal sandbox init \  
&& cabal sandbox add-source ../z3-haskell \  
&& cabal sandbox add-source ../bacon-core \  
# && cabal sandbox add-source ../bacon-gui \  
&& cabal install --reinstall --force-reinstalls  
  
ENV PATH ${PATH}:/home/bacon/bacon-main/.cabal-sandbox/bin  
  
RUN cd /home/bacon && clang -g -S bacon-doc/examples/example1.c -emit-llvm &&
bacon-preprocessor/smoke example1.ll  
RUN cd /home/bacon && clang -g -S bacon-doc/examples/example2.c -emit-llvm &&
bacon-preprocessor/smoke example2.ll  
RUN cd /home/bacon && clang -g -S bacon-doc/examples/example3.c -emit-llvm &&
bacon-preprocessor/smoke example3.ll  
RUN cd /home/bacon && clang -g -S bacon-doc/examples/example4.c -emit-llvm &&
bacon-preprocessor/smoke example4.ll  
RUN cd /home/bacon && clang -g -S bacon-doc/examples/example5.c -emit-llvm &&
bacon-preprocessor/smoke example5.ll  

