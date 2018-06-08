FROM ubuntu:artful-20171116  
ENV PATH="/home/travis/.evm/bin:/home/travis/.cask/bin:${PATH}"  
RUN apt update && \  
apt install -y git ssh tar gzip ca-certificates \  
python ruby curl \  
libxaw7 libx11-xcb1 libxfixes3 gnutls-bin  
  
RUN curl -fsSkL
https://gist.githubusercontent.com/sigma/a78ac2694e3b0404566cb443a2cf0eec/raw
-o /travis.sh && bash /travis.sh  
  
ARG EMACS="emacs-git-snapshot-travis"  
RUN evm install $EMACS \--use --skip  
  

