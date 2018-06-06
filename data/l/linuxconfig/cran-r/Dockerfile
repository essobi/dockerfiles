FROM debian:8  
MAINTAINER Lubos Rendek <web@linuxconfig.org>  
  
# Alter source list  
RUN sed -i '1p' /etc/apt/sources.list  
RUN sed -i '0,/ /s//-src /' /etc/apt/sources.list  
RUN sed -i 's/httpredir/ftp.us/g' /etc/apt/sources.list  
RUN apt-get update  
  
# Install required tools  
RUN apt-get install -y curl  
  
# Install build dependencies  
RUN apt-get build-dep -y r-base  
  
# Download and decompress latest r-cran version  
RUN curl -s https://cran.r-project.org/src/base/R-3/R-3.2.1.tar.gz | tar xz  
  
# r-cran compilation & installation  
WORKDIR /R-3.2.1  
  
# Compile and install  
RUN ./configure; make; make install  
  
WORKDIR /  

