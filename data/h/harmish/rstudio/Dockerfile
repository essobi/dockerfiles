FROM rocker/tidyverse  
  
# install latex fonts  
RUN R -e "install.packages(\"extrafont\"); library(extrafont);
font_install('fontcm', prompt = FALSE)"  
  
RUN echo "root:root" | chpasswd && \  
echo 'auth-minimum-user-id=0' >> /etc/rstudio/rserver.conf  

