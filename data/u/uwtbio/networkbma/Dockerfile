# This is the Dockefile to build GUIdock (kristiyanto/guidock)  
# https://hub.docker.com/r/uwtbio/networkbma/  
# Base Docker Image  
FROM bioconductor/release_base  
  
  
# Environtment  
ENV PATH /usr/lib/rstudio-server/bin/:$PATH  
ENV LANG en_US.UTF-8  
EXPOSE 8787  
# Maintainer  
MAINTAINER Daniel Kristiyanto, danielkr@uw.edu  
  
# Install Boost C++  
RUN apt-get update  
RUN sudo apt-get -q -y install libboost-all-dev  
RUN apt-get clean  
  
# Install Openblas  
RUN echo '/opt/OpenBLAS/lib' > /etc/ld.so.conf.d/openblas.conf  
ADD openblas.sh /tmp/openblash.sh  
RUN bash /tmp/openblash.sh  
  
# Copy NetworkBMA package  
COPY networkBMA_2.10.11.tar.gz /tmp/networkBMA_2.10.11.tar.gz  
  
# Install dependencies  
RUN echo 'source("http://bioconductor.org/biocLite.R")' >> /tmp/packages.R  
RUN echo 'biocLite("BMA")' >> /tmp/packages.R  
RUN echo 'biocLite("RcppArmadillo")' >> /tmp/packages.R  
RUN echo 'biocLite("Rcpp")' >> /tmp/packages.R  
RUN echo 'biocLite("RcppEigen")' >> /tmp/packages.R  
  
# Install Network BMA  
RUN echo 'install.packages("/tmp/networkBMA_2.10.11.tar.gz", repos = NULL,
type="source", dependencies=TRUE)' >> /tmp/packages.R \ && Rscript
/tmp/packages.R  
  

