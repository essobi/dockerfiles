FROM fedora:25  
MAINTAINER Jens Petersen <petersen@fedoraproject.org>  
# Haskell ghc, cabal, stack  
RUN dnf -y update && dnf clean all  
RUN dnf -y install dnf-plugins-core ;\  
dnf -y copr enable petersen/stack ;\  
dnf -y install ghc cabal-install stack hscolour git-core ghc-rpm-macros rpm-
build dos2unix cabal-rpm zlib-devel &&\  
dnf clean all  
  
CMD [ "/bin/bash" ]  

