FROM ubuntu:17.10  
MAINTAINER Johannes Mitlmeier <dev.jojomi@yahoo.com>  
  
# udpate base system  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get --yes update && \  
apt-get --yes dist-upgrade  
  
# setup TeX packages  
RUN apt-get --yes --no-install-recommends --no-install-suggests install
texlive texlive-lang-english texlive-lang-german \  
texlive-latex-base texlive-latex-recommended texlive-latex-extra && \  
apt-get --yes install texlive-xetex texlive-luatex  
RUN apt-get --yes install fonts-linuxlibertine fonts-inconsolata fonts-oflb-
asana-math  
  
# setup tlmgr  
RUN apt-get --yes install wget xzdec && \  
tlmgr init-usertree && \  
# cleanup  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# install custom packages  
# RUN tlmgr install genealogytree  
VOLUME /src  
WORKDIR /src  
CMD pdflatex /src/document.tex  

