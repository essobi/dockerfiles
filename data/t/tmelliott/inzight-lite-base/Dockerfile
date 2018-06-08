FROM ubuntu:14.04  
MAINTAINER "Tom Elliott" tom.elliott@auckland.ac.nz  
  
# add metadata that tells us the URL that hosts this Dockerfile  
# NOTE: LABEL does not work with docker 1.2.0  
#LABEL
dockerfile=https://raw.githubusercontent.com/iNZightVIT/docker_images/master/inzight-
lite/Dockerfile  
## ------------------------------------------------------------------ Which
version of R do you need?  
#ENV R_VERSION 3.2.0  
# Add the CRAN PPA to get all versions of R  
RUN echo 'deb http://cran.stat.auckland.ac.nz/bin/linux/ubuntu trusty/'
>/tmp/cranppa.list \  
&& cp /tmp/cranppa.list /etc/apt/sources.list.d/ \  
&& rm /tmp/cranppa.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9  
  
# Install R (including recommended packages)  
RUN apt-get -y update \  
&& apt-get -y install --allow-unauthenticated r-base  
  
## ------------------------------------------------------------------ What
version of Shiny do you want (URL)?  
ENV SHINY_VERSION http://download3.rstudio.org/ubuntu-12.04/x86_64/shiny-
server-1.3.0.403-amd64.deb  
  
# Install shiny  
RUN apt-get -y update \  
&& apt-get -y install --no-install-recommends \  
gdebi-core \  
wget  
  
RUN wget -O shiny-server.deb ${SHINY_VERSION} \  
&& gdebi -n shiny-server.deb \  
&& rm -f shiny-server.deb  
  
RUN apt-get -y update \  
&& apt-get -y install --no-install-recommends \  
make \  
gcc \  
g++ \  
&& R -e "install.packages('rmarkdown', repos='http://cran.rstudio.com/',
lib='/usr/lib/R/site-library')"  
  
## Install some additional packages for the CAS app:  
RUN apt-get -y update \  
&& apt-get -y install \  
libcurl4-openssl-dev \  
libxml2-dev \  
&& R -e "install.packages(c('devtools', 'shiny', 'DT'),
repos='http://cran.rstudio.com/', lib='/usr/lib/R/site-library')" \  
&& R -e "devtools::install_github('ramnathv/rCharts')"  

