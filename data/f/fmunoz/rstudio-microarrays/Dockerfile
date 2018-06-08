FROM rocker/rstudio:latest  
MAINTAINER "Felipe de Jesus Muñoz Gonzalez" fmunoz@lcg.unam.mx  
  
RUN apt-get -y -q dist-upgrade  
  
#RUN apt-get -y update -qq && apt-get -y upgrade  
#RUN apt-get install -y --no-install-recommends apt-utils software-properties-
common  
#RUN sudo add-apt-repository -y ppa:ubuntu-toolchain-r/test  
  
RUN apt-get -y update -qq && apt-get -y upgrade  
  
RUN apt-get install -y --no-install-recommends libpangoft2-1.0-0 \  
libxt-dev \  
xvfb \  
xauth \  
xfonts-base \  
libglib2.0-0 \  
libglib2.0-bin \  
libpango-1.0-0 \  
libxml2-dev \  
libglib2.0-dev \  
libgdk-pixbuf2.0-dev \  
libatk1.0-dev \  
libssl1.0.0 \  
libpangocairo-1.0-0 \  
libcairo2 \  
libcairo2-dev \  
fonts-dejavu \  
gfortran \  
libssh2-1-dev \  
r-cran-xml \  
r-cran-plyr \  
r-cran-ggplot2 \  
r-cran-gplots \  
libnlopt-dev \  
xml-core \  
lsb-release \  
libssl-dev \  
gcc && apt-get clean  
  
  
  
  

