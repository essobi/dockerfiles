##Setting the base  
FROM ubuntu:xenial  
#Dockerfile author / maintainer  
MAINTAINER Ashrith Barthur bartha et code0 do org  
  
#Installing r-base on ubuntu.  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
pandoc \  
r-base vim texlive python binutils gfortran \  
libpcre3 libpcre3-dev lzma liblzma-dev libbz2-dev \  
libcurl4-openssl-dev libssl-dev libxml2-dev \  
gdebi-core \  
python-setuptools \  
python-doc python-tk python2.7-doc binfmt-support texlive-latex-extra python-
pip \  
build-essential curl git htop man unzip wget locales locales-all  
# pip install kaggle  
RUN apt-get --purge remove openjdk* && \  
echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true"
| debconf-set-selections && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" >
/etc/apt/sources.list.d/webupd8team-java-trusty.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \  
apt-get update && \  
apt-get install -y oracle-java8-installer oracle-java8-set-default && \  
apt-get clean all && \  
R CMD javareconf  
RUN echo "options(unzip=\"unzip\",digits = 5, scipen = 16,
repos=\"http://cran.cnr.berkeley.edu/\")" > ~/.Rprofile && \  
echo "pkglist <\-
c(\"rJava\",\"lattice\",\"data.table\",\"rmarkdown\",\"h2o\",\"sparklyr\",\"plotly\",\"tidyverse\")
\\n \  
install.packages(pkglist) \\n \  
q()" > ~/install.R && \  
cat ~/install.R && \  
R --no-save -e "source(\"~/install.R\")"  
RUN echo ":set fileencoding=utf-8 \\n \  
:set showmode \\n\  
:set ruler\\n\  
:set encoding=utf-8\\n\  
:set number\\n\  
:syntax on\\n\  
syntax enable\\n\  
set background=light\\n\  
call plug#begin('~/.vim/plugged')\\n\  
Plug 'vim-pandoc/vim-pandoc'\\n\  
Plug 'vim-pandoc/vim-pandoc-syntax'\\n\  
Plug 'vim-pandoc/vim-rmarkdown'\\n\  
Plug 'altercation/vim-colors-solarized'\\n\  
Plug 'jalvesaq/Nvim-R'\\n\  
Plug 'roxma/nvim-completion-manager'\\n\  
Plug 'gaalcaras/ncm-R'\\n\  
call plug#end()\\n\  
colorscheme solarized" > ~/.vimrc && \  
vim -E ":PlugInstall;:q!"  
  
#RUN pip install kaggle  
#Load your kaggle API key at $HOME/.kaggle/kaggle.json  
  
  
# Things to do  
# 1. Clean up the code  
# 2. Add Comments  
# 3. Break docker RUN into permanent and dynamic runs, so to keep layers
clean.  
  

