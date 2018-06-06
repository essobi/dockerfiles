FROM ubuntu:16.04  
MAINTAINER Junji Hashimoto "junji.hashimoto@gmail.com"  
RUN apt update -qq && \  
apt -y --force-yes install \  
curl libssl-dev gnupg gnupg2 \  
perl make automake gcc libgmp-dev libffi-dev libz-dev xz* tar git libncurses-
dev  
RUN curl -sSL https://get.haskellstack.org/ | sh  
RUN stack setup 8.0.2  
RUN stack install clash-ghc  
RUN mkdir /src  
WORKDIR /src  
ENV PATH /root/.stack/global-project/.stack-
work/install/x86_64-linux/lts-9.13/8.0.2/bin:/root/.stack/snapshots/x86_64-linux/lts-9.13/8.0.2/bin:/root/.stack/programs/x86_64-linux/ghc-8.0.2/bin:/root/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
ENV GHC_PACKAGE_PATH /root/.stack/global-project/.stack-
work/install/x86_64-linux/lts-9.13/8.0.2/pkgdb:/root/.stack/snapshots/x86_64-linux/lts-9.13/8.0.2/pkgdb:/root/.stack/programs/x86_64-linux/ghc-8.0.2/lib/ghc-8.0.2/package.conf.d  
ENV HASKELL_DIST_DIR .stack-work/dist/x86_64-linux/Cabal-1.24.2.0  
ENV HASKELL_PACKAGE_SANDBOX
/root/.stack/snapshots/x86_64-linux/lts-9.13/8.0.2/pkgdb  
ENV HASKELL_PACKAGE_SANDBOXES /root/.stack/global-project/.stack-
work/install/x86_64-linux/lts-9.13/8.0.2/pkgdb:/root/.stack/snapshots/x86_64-linux/lts-9.13/8.0.2/pkgdb:  

