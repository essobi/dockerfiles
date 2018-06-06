# Galaxy - ChemicalToolBox  
FROM quay.io/bgruening/galaxy:18.05  
MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com  
  
ENV GALAXY_CONFIG_BRAND=ChemicalToolBox  
  
# Include all needed scripts and libraries from the host  
# compressed archives will be extracted automatically  
#ADD ./Jmoleditor.tar.bz2 /galaxy-central/  
ADD chemicaltoolbox_tools.yml $GALAXY_ROOT/tools.yaml  
RUN install-tools $GALAXY_ROOT/tools.yaml && \  
/tool_deps/_conda/bin/conda clean --tarballs --yes > /dev/null && \  
rm /export/galaxy-central/ -rf && \  
mkdir -p $GALAXY_HOME/workflows  
  
# install unique wrapper  
#RUN install-repository "--url http://toolshed.g2.bx.psu.edu/ -o bgruening
--name unique --panel-section-id filter"  

