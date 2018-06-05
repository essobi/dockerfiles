FROM ubuntu:16.04  
  
# User and workdir settings:  
USER root  
WORKDIR /root  
CMD /bin/bash  
  
# build requirements  
RUN apt-get update && apt-get install -y build-essential curl autoconf
automake git-core libtool vim  
  
# ROOT dependency  
RUN apt-get install -y libroot-graf2d-postscript-dev libroot-graf3d-g3d-dev \  
libroot-math-foam-dev libroot-math-minuit-dev \  
libroot-math-physics-dev libroot-math-mathmore-dev \  
libroot-roofit-dev root-system-bin  
  
# doxygen html  
RUN apt-get install -y doxygen graphviz poppler-utils pdftk  
  
# latex manual  
RUN apt-get install -y texlive-latex-recommended texlive-latex-extra texlive-
fonts-extra texlive-science  
  
# clean up:  
RUN apt-get autoclean  

