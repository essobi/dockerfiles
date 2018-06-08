FROM haskell  
  
# make sure apt-get install doesn't do stupid  
ENV DEBIAN_FRONTEND noninteractive  
ENV INSTALL_ONLY -y --force-yes --no-install-recommends  
  
# Install predepends  
RUN apt-get update && apt-get install $INSTALL_ONLY \  
git vim curl build-essential \  
exuberant-ctags libcurl4-openssl-dev mercurial \  
ghc-mod  
RUN apt-get clean  
  
# install vim-now  
RUN curl https://raw.githubusercontent.com/begriffs/haskell-vim-
now/master/install.sh | bash  
  
# install custom vim settings  
ADD ./add/vimrc.local /root/.vimrc.local  
  
# remove cabal bloat  
RUN rm /root/.cabal -rf  
  
# app directory  
RUN mkdir /project  
WORKDIR /project  
  
# auto update vundle  
RUN vim -c ':VundleInstall' -c 'qa!'  

