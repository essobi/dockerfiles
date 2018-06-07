# GPLv3  
FROM debian:jessie  
MAINTAINER njanetos <nejanetos@gmail.com>  
LABEL Description="Build environment for 'Reputation Dynamics in a Market for
Illicit Drugs'"  
## add latex, python, r-base, as well as useful dependencies  
RUN rm -rf /var/lib/apt/lists/* && \  
apt-get update && \  
apt-get install -y \  
# latex  
latexmk \  
texlive \  
texlive-xetex \  
texlive-luatex \  
# python  
python3 \  
python3-pip \  
python3-tk \  
# r  
r-base \  
# utilities  
gfortran \  
git \  
libfreetype6-dev \  
liblapack-dev \  
libpng-dev \  
make \  
pdftk \  
pkg-config \  
poppler-utils \  
p7zip-full \  
wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
## install python packages  
RUN mkdir cache && \  
pip3 install --download-cache /cache \  
matplotlib \  
numpy \  
pandas \  
scipy \  
seaborn \  
statsmodels && \  
rm -rf /cache  
  
# set CRAN mirror  
RUN echo 'options(repos = c(CRAN = "http://cran.r-project.org"))' >>
/etc/R/Rprofile.site  
  
## create a working directory  
RUN mkdir working  
  
## copy github files to working directory  
COPY . working/  
  
## build everything  
RUN cd /working/ && ./build.sh  

