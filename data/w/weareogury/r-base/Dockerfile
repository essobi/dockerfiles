FROM ubuntu:16.04  
  
MAINTAINER Ogury Team <it@ogury.co>  
  
ENV CRAN_URL "http://cran.rstudio.com"  
  
RUN echo "deb ${CRAN_URL}/bin/linux/ubuntu xenial/" >
/etc/apt/sources.list.d/cran.fhcrc.org.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9  
  
RUN apt-get update && \  
apt-get install -y r-base=3.3.2* \  
libcurl4-gnutls-dev \  
libxml2-dev \  
libssl-dev \  
jq \  
postgresql-client \  
python-dev \  
python2.7 \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
pip install awscli && \  
pip install csvkit  
  
  
# install R and customed R packages  
RUN R -e "install.packages('devtools', repos='${CRAN_URL}');"  
RUN R -e "library(devtools); \  
install_version( package = 'assertthat', version = '0.1',
repos='${CRAN_URL}'); \  
install_version( package = 'dismo', version = '1.1-1', repos='${CRAN_URL}'); \  
install_version( package = 'doParallel', version = '1.0.10',
repos='${CRAN_URL}'); \  
install_version( package = 'foreach', version = '1.4.3', repos='${CRAN_URL}');
\  
install_version( package = 'functional', version = '0.6',
repos='${CRAN_URL}'); \  
install_version( package = 'ggplot2', version = '2.2.1', repos='${CRAN_URL}');
\  
install_version( package = 'Matrix', version = '1.2-7.1',
repos='${CRAN_URL}'); \  
install_version( package = 'plyr', version = '1.8.4', repos='${CRAN_URL}'); \  
install_version( package = 'dplyr', version = '0.5.0', repos='${CRAN_URL}'); \  
install_version( package = 'numbers', version = '0.6-1', repos='${CRAN_URL}');
\  
install_version( package = 'RUnit', version = '0.4.31', repos='${CRAN_URL}');
\  
install_version( package = 'rjson', version = '0.2.15', repos='${CRAN_URL}');"  
# test if R package are correctly installed  
RUN R -e "library(devtools); \  
library(rjson); \  
library(ggplot2); \  
library(plyr); \  
library(RUnit); \  
library(Matrix); \  
library(doParallel); \  
library(foreach); \  
library(assertthat); \  
library(rjson);"  

