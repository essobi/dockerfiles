# Copyright (c) Jupyter Development Team.  
# Distributed under the terms of the Modified BSD License.  
FROM marcsaric/datascience-notebook  
  
LABEL maintainer="Marc Saric <marc.saric@gmx.de>"  
  
USER root  
  
# R pre-requisites  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
USER $NB_USER  
  
# Add TCGAWorkflow  
COPY installTCGAWorkflow.R /home/$NB_USER  
RUN R -f /home/$NB_USER/installTCGAWorkflow.R  
  

