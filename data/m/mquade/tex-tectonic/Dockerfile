FROM continuumio/miniconda3:latest  
  
MAINTAINER info@markusqua.de  
  
RUN apt-get update && \  
apt-get install \  
ruby-dev \  
git \  
g++ \  
make \  
-y  
  
RUN \curl -sSL https://get.rvm.io | bash -s stable --ruby  
RUN /bin/bash -c "source /usr/local/rvm/scripts/rvm"  
  
RUN conda config --add channels conda-forge && \  
conda config --add channels pkgw-forge && \  
conda install tectonic -y  

