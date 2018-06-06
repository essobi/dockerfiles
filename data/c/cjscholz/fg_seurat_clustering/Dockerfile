############################################################  
# Dockerfile to run the Seurat preprocessing and clustering  
# of single-cell RNA-seq data in FAST Genomics format  
############################################################  
  
# base image of Bioconductor  
FROM bioconductor/release_core2  
  
# File Author / Maintainer  
MAINTAINER Claus J. Scholz <cscholz@uni-bonn.de>  
  
# start the installation  
ADD ./install_scripts /opt/install_scripts  
RUN sudo apt-get update  
RUN apt-get -y install default-jre  
RUN Rscript /opt/install_scripts/install_Seurat.R  
  
# run the command to start the Seurat pipeline  
ADD ./scripts /opt/scripts  
ADD ./config /opt/config  
CMD ["Rscript", "--default-
packages=base,utils,grDevices,graphics,stats,methods",
"/opt/scripts/raw2cluster.R"]  

