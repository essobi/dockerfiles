FROM ubuntu:16.04  
  
ADD install_packages.r /  
ADD Renviron.site /  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends software-properties-common \  
&& apt-add-repository -y "deb http://cran.rstudio.com/bin/linux/ubuntu
xenial/" \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 \  
&& apt-get update \  
&& apt-get -y --no-install-recommends install \  
r-base-dev \  
libxml2-dev \  
libcairo2-dev \  
libssl-dev \  
libcurl4-openssl-dev \  
texlive texinfo texlive-fonts-extra \  
openjdk-8-jdk \  
r-cran-rjava \  
&& apt-get autoremove \  
&& apt-get autoclean \  
&& mv /Renviron.site /etc/R/ \  
&& Rscript /install_packages.r \  
&& rm /install_packages.r \  

