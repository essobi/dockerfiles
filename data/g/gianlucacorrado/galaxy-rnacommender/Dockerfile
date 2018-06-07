# Galaxy - RNAcommender  
FROM quay.io/bgruening/galaxy:16.04  
  
MAINTAINER Gianluca Corrado gianluca.corrado@unitn.it  
  
ENV GALAXY_CONFIG_BRAND="RNAcommender" \  
GALAXY_CONFIG_CONDA_AUTO_INSTALL=True \  
GALAXY_CONFIG_CONDA_AUTO_INIT=True \  
GALAXY_CONFIG_CONDA_ENSURE_CHANNELS=r,bioconda,iuc,kundajelab  
  
# Install RNAcommender  
ADD rnacommender.yaml $GALAXY_ROOT/tools.yaml  
RUN install-tools $GALAXY_ROOT/tools.yaml  

