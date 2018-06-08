# Galaxy - GalaxyP  
FROM bgruening/galaxy-sequence-tools:17.09  
MAINTAINER Björn A. Grüning, bjoern.gruening@gmail.com  
  
ENV GALAXY_CONFIG_BRAND Galaxy for Proteomic Research  
  
# Install tools  
ADD galaxyp.yaml $GALAXY_ROOT/tools.yaml  
  
RUN install-tools $GALAXY_ROOT/tools.yaml && \  
/tool_deps/_conda/bin/conda clean --tarballs  
  
# Add data library defintion file  
ADD library_data.yaml $GALAXY_ROOT/library_data.yaml  
  
# Add workflows to the Docker image  
ADD ./workflows/* $GALAXY_HOME/workflows/  
  
ENV GALAXY_CONFIG_TOOL_PATH=/galaxy-central/tools/  
  
RUN startup_lite && \  
galaxy-wait && \  
workflow-install --workflow_path $GALAXY_HOME/workflows/ -g
http://localhost:8080 -u $GALAXY_DEFAULT_ADMIN_USER -p
$GALAXY_DEFAULT_ADMIN_PASSWORD && \  
setup-data-libraries -i $GALAXY_ROOT/library_data.yaml -g
http://localhost:8080 -u $GALAXY_DEFAULT_ADMIN_USER -p
$GALAXY_DEFAULT_ADMIN_PASSWORD  
  

