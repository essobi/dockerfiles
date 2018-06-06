FROM rocker/rstudio  
  
MAINTAINER "Christoph Burow" christoph.burow@gmx.net  
  
RUN apt-get update -qq \  
&& apt-get -y --no-install-recommends install \  
libxt-dev \  
libcairo2-dev \  
libxml2-dev \  
libx11-dev \  
libcgal-dev \  
libglu1-mesa-dev \  
libmagick++-dev \  
libhunspell-dev \  
## Build JAGS-4 from source (debian:stable is still on JAGS-3.x.y)  
&& wget https://sourceforge.net/projects/mcmc-
jags/files/JAGS/4.x/Source/JAGS-4.2.0.tar.gz -O jags.tar.gz \  
&& tar -xf jags.tar.gz \  
&& cd JAGS* && ./configure && make && make install \  
&& cd / && rm -rf jags.tar.gz JAGS* \  
## Install R packages  
&& . /etc/environment \  
&& install2.r --error \  
\--repos 'http://www.bioconductor.org/packages/release/bioc' \  
\--repos "https://mran.microsoft.com/" \  
\--deps "TRUE" \  
rgl devtools ggplot2 tidyverse rmarkdown

