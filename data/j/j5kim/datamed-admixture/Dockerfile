### set the base image to Ubuntu  
FROM rocker/rstudio  
  
### File author / maintainer  
MAINTAINER Jihoon Kim "j5kim@ucsd.edu"  
  
### change a working directory to /opt  
WORKDIR /opt  
  
### update the repository source list, install dependent packages,  
### install R add-on packages, and install iadmix  
RUN apt-get update -y && \  
apt-get install -y git && \  
git clone https://github.com/jihoonkim/DataMed-Admixture.git && \  
Rscript /opt/DataMed-Admixture/provision/install_Rpackages.R && \  
bash /opt/DataMed-Admixture/provision/install_iadmix.sh  
  
### change a working directory to /opt/ancestry  
WORKDIR /opt/ancestry

