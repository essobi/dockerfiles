# docker build --rm -t r .  
FROM ubuntu:16.04  
  
RUN apt-get update && \  
apt-get -y install software-properties-common apt-transport-https  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
E298A3A825C0D65DFD57CBB651716619E084DAB9 && \  
add-apt-repository 'deb [arch=amd64,i386]
https://cran.rstudio.com/bin/linux/ubuntu xenial/' && \  
apt-get update && \  
apt-get -y install r-base build-essential \  
libxml2-dev libssl-dev git r-base-dev \  
libcurl4-openssl-dev  
  
ADD Rprofile /root/.Rprofile  

