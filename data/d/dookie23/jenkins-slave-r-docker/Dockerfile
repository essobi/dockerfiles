FROM dookie23/jenkins-slave-r-docker:r-base  
  
MAINTAINER "Agustín Cañas" acanas@gradiant.org  
  
USER root  
  
RUN R -e "install.packages(c('dplyr'), repos='http://cloud.r-project.org/')"  
# Json packages  
RUN R -e "install.packages(c('RJSONIO', 'rjson'),
repos='http://cloud.r-project.org/')"  
# Plumber (REST services)  
RUN R -e "install.packages(c('plumber'), repos='http://cloud.r-project.org/')"  
  
USER jenkins

