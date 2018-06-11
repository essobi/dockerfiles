# xCell Python module and CLI for xCell  
# This is a wraper of xCell for CLI and python module use  
# for the official xCell R distribution see  
# https://github.com/dviraran/xCell  
# If used cite:  
# Aran D, Hu Z, Butte AJ. xCell: digitally portraying the tissue cellular  
# heterogeneity landscape. Genome Biol. 2017 Nov 15;18(1):220. doi:  
# 10.1186/s13059-017-1349-1. PubMed PMID: 29141660; PubMed Central PMCID:  
# PMC5688663.  
FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y gcc g++ perl python automake make \  
wget git curl libdb-dev \  
zlib1g-dev bzip2 libncurses5-dev \  
texlive-latex-base \  
gfortran \  
build-essential libghc-zlib-dev libncurses-dev libbz2-dev liblzma-dev
libpcre3-dev libxml2-dev \  
libblas-dev gfortran git unzip ftp libzmq3-dev nano ftp fort77 libreadline-dev
\  
libcurl4-openssl-dev libx11-dev libxt-dev \  
x11-common libcairo2-dev libpng12-dev libreadline6-dev libjpeg8-dev pkg-config
libtbb-dev \  
&& apt-get clean  
  
ENV SRC /usr/local/src  
ENV BIN /usr/local/bin  
  
WORKDIR $SRC  
  
ENV R_VERSION=R-3.4.1  
RUN curl https://cran.r-project.org/src/base/R-3/$R_VERSION.tar.gz -o
$R_VERSION.tar.gz && \  
tar xvf $R_VERSION.tar.gz && \  
cd $R_VERSION && \  
./configure --with-x=no && make && make install  
  
RUN apt-get install -y software-properties-common python-software-properties  
RUN add-apt-repository ppa:jonathonf/python-3.6 && \  
apt-get update && \  
apt-get install -y python3.6 \  
python3-pip  
  
RUN Rscript -e
'source("http://bioconductor.org/biocLite.R");library(BiocInstaller);biocLite(pkgs=c("GSEABase","GSVA"),dep=TRUE)'  
  
RUN apt-get install -y libssl-dev libssh2-1-dev && \  
Rscript -e 'install.packages("devtools",repos =
"http://cran.us.r-project.org")' && \  
Rscript -e 'library(devtools);devtools::install_github("jason-
weirather/R-xCell")'  
  
RUN pip3 install --upgrade pip  
RUN pip3 install xcell==1.1.0.1  
  
ENV HOME /root  
WORKDIR /root  

