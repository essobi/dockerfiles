# Galaxy - RAD-Seq  
FROM bgruening/galaxy-ngs-preprocessing  
  
MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com  
  
ENV GALAXY_CONFIG_BRAND="RAD-Seq" \  
GALAXY_CONFIG_ENABLE_BETA_TOOL_COMMAND_ISOLATION=True \  
GALAXY_CONFIG_CONDA_AUTO_INSTALL=True \  
GALAXY_CONFIG_CONDA_AUTO_INIT=True  
# Install RAD seq tools  
ADD rad_seq_tools.yml $GALAXY_ROOT/tools.yaml  
RUN install-tools $GALAXY_ROOT/tools.yaml  

