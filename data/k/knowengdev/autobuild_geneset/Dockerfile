FROM ubuntu:14.04  
MAINTAINER Jing Ge <jingge2@illinois.edu>  
  
ENV SRC_LOC /home  
  
# Install packages  
RUN apt-get update && \  
apt-get install -y vim python3-pip git libblas-dev liblapack-dev libatlas-
base-dev gfortran libfreetype6-dev libxft-dev  
  
RUN pip3 install -I numpy==1.11.1 pandas==0.18.1 scipy==0.18.0 scikit-
learn==0.17.1 matplotlib==1.4.2 knpackage pyyaml  
  
# Clone from github  
RUN git clone https://candicegjing:jacky1219@github.com/KnowEnG-
Research/GeneSet_Characterization_Pipeline.git ${SRC_LOC}  
  
RUN rm -rf {SRC_LOC}/build {SRC_LOC}/input_data {SRC_LOC}/test {SRC_LOC}/docs  
  
# Set up working directory  
WORKDIR ${SRC_LOC}  

