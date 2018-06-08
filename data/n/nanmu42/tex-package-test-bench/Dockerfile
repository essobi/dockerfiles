FROM ubuntu:xenial  
  
LABEL Description="Package testbench for LaTeX and friends, based on MiKTeX by
Christian Schenk, Ubuntu 16.04" Vendor="nanmu42" Version="0.5.0"  
  
# Install MiKTeX  
RUN apt-get update  
RUN apt-get install apt-transport-https -y  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
D6BC243565B2087BC3F897C9277A7293F59E4889  
RUN echo "deb http://miktex.org/download/ubuntu xenial universe" | tee
/etc/apt/sources.list.d/miktex.list  
RUN apt-get update  
RUN apt-get install miktex -y  
  
# install make for automated task  
RUN apt-get install build-essential -y  
  
# install perl for latexmk usage  
RUN apt-get install perl -y  
  
# MiKTeX Packages  
RUN initexmf --admin --force --mklinks  
RUN mpm --admin --install amsfonts  
RUN mpm --admin --install fandol  
RUN mpm --admin --install latexmk  
RUN initexmf --admin --mkmaps  
RUN initexmf --admin --update-fndb  
  
RUN useradd -md /miktex miktex  
USER miktex  
RUN mkdir /miktex/work  
RUN mkdir /miktex/.miktex  
WORKDIR /miktex/work  

