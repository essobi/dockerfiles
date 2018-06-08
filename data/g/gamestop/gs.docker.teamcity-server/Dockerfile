FROM jetbrains/teamcity-server:2017.2.2  
ENV TEAMCITY_DATA_PATH=/app/teamcity/datadir  
ENV TEMP_DIR=/temp  
  
COPY scripts /scripts  
  
RUN chmod +x /scripts/*.sh  
  
# Install software  
RUN /scripts/install-mysql-jdbc.sh  
  
# Install plugins  
RUN /scripts/install-plugins.sh  
  
# Bootstraps  
ENTRYPOINT [ "/bin/bash","./scripts/bootstrap.sh"]  

