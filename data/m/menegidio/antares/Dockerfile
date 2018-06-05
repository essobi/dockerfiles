#FROM bigscience/docker-galaxy-stable  
FROM menegidio/base  
MAINTAINER Fabiano Menegidio <fabiano.menegidio@biology.bio.br>  
  
ENV GALAXY_CONFIG_BRAND=QIIME \  
GALAXY_CONFIG_CONDA_AUTO_INSTALL=True \  
GALAXY_CONFIG_CONDA_AUTO_INIT=True  
  
# Add config files  
ADD config/tool_conf.xml $GALAXY_ROOT/config/  
  
# Install Tools  
ADD config/qiime.yaml $GALAXY_ROOT/tools.yaml  
RUN install-tools $GALAXY_ROOT/tools.yaml  
  
VOLUME ["/export/", "/data/", "/var/lib/docker"]  
  
# Expose port 80 (webserver), 21 (FTP server), 8800 (Proxy)  
EXPOSE :80  
EXPOSE :21  
EXPOSE :22  
EXPOSE :8800  
# Autostart script that is invoked during container start  
CMD ["/usr/bin/startup"]  

