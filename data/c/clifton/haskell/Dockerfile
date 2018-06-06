FROM clifton/debian-base  
MAINTAINER Clifton <cliftonk@gmail.com>  
  
RUN echo "deb http://cdn.debian.net/debian/ testing main non-free contrib" >>
/etc/apt/sources.list  
  
RUN apt-get update  
RUN apt-get install -y wget zlib1g-dev bzip2 libncursesw5 gcc apt-utils make
libgmp-dev  
  
RUN ln -s /usr/lib/x86_64-linux-gnu/libgmp.so /usr/lib/x86_64-linux-
gnu/libgmp.so.3  
  
# GHC install  
RUN wget http://www.haskell.org/ghc/dist/7.8.2/ghc-7.8.2-x86_64-unknown-linux-
deb7.tar.bz2  
  
RUN tar xfj ghc-7.8.2-x86_64-unknown-linux-deb7.tar.bz2  
RUN cd ghc-7.8.2 && ./configure && make install && ghc --version  
  
# clean up GHC install files  
RUN rm -fr ghc-7.8.2-x86_64-unknown-linux-deb7.tar.bz2 ghc-7.8.2  
  
# install cabal  
RUN wget http://hackage.haskell.org/package/cabal-install-1.18.0.3/cabal-
install-1.18.0.3.tar.gz  
RUN tar xvfz cabal-install-1.18.0.3.tar.gz  
RUN (cd cabal-install-1.18.0.3 && ./bootstrap.sh)  
RUN ln -s /.cabal/bin/cabal /usr/bin/cabal && cabal --version  
RUN cabal update  
  
# clean up cabal files  
RUN rm -fr cabal-install-1.18.0.3*  
  
# clean up apt  
RUN apt-get clean  
  
ENV PATH
/.cabal/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  

