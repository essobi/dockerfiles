############ ITMAT FUN #############################################  
# Base image is from Ubuntu 16.04 aka 'Xenial Xerus'  
# Provides Python 2.7.12  
# ToDo: consider losing weight with Alpine Linux!  
####################################################################  
  
FROM ubuntu:16.04  
  
MAINTAINER Jacintha Mack Smith <j.mack-smith@imperial.ac.uk>  
MAINTAINER David Mosen <d.mosen-ansorena@imperial.ac.uk>  
  
###############################################################  
# update package lists and install some useful bits and pieces:  
###############################################################  
  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
curl \  
git \  
graphviz \  
libxml2-dev \  
libcurl4-openssl-dev \  
python-pip \  
software-properties-common \  
sudo \  
unzip \  
vim \  
wget && \  
rm -rf /var/lib/apt/lists/*  
  
  
#########################################################  
# install RUFFUS:  
#########################################################  
  
RUN pip install --upgrade pip  
RUN pip install ruffus --upgrade  
  
#########################################################  
# install PLINK:  
#########################################################  
  
ENV PLINK_VERSION 1.9  
ENV PLINK_NO plink170113  
ENV PLINK_HOME /usr/local/plink  
  
RUN wget https://www.cog-
genomics.org/static/bin/$PLINK_NO/plink_linux_x86_64.zip && \  
unzip plink_linux_x86_64.zip -d /usr/local/ && \  
rm plink_linux_x86_64.zip && \  
cd /usr/local/bin && \  
ln -s $PLINK_HOME plink  
  
#########################################################  
# Install R and friends:  
#########################################################  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
E298A3A825C0D65DFD57CBB651716619E084DAB9 && \  
add-apt-repository 'deb [arch=amd64,i386]
https://cran.rstudio.com/bin/linux/ubuntu xenial/'  
RUN apt-get update && apt-get install -y r-base r-cran-littler  
  
# Create install script for packages that uses biocLite:  
  
RUN echo '#!/usr/bin/env r' > /usr/local/bin/install.r && \  
echo 'library(utils)' >> /usr/local/bin/install.r && \  
echo 'source("https://bioconductor.org/biocLite.R")' >>
/usr/local/bin/install.r && \  
echo 'lib.loc <\- "/usr/local/lib/R/site-library"' >> /usr/local/bin/install.r
&& \  
echo 'biocLite(commandArgs(TRUE), lib.loc)' >> /usr/local/bin/install.r && \  
chmod 755 /usr/local/bin/install.r  
  
# install required R packages:  
  
RUN Rscript /usr/local/bin/install.r \  
ggplot2 \  
plyr \  
qqman \  
data.table \  
geneplotter \  
SNPRelate  

