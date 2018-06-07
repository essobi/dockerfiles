FROM ubuntu:16.04  
# install texlive  
RUN apt-get update && \  
apt-get install -y biber inkscape texlive-full wget && \  
#  
# fix for titlesec package  
wget http://mirrors.ctan.org/macros/latex/contrib/titlesec/titlesec.sty -O
/usr/share/texlive/texmf-dist/tex/latex/titlesec/titlesec.sty && \  
#  
# clean -up  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/latex"]  
WORKDIR /latex  

