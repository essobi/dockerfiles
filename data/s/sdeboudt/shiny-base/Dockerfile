FROM openanalytics/r-base  
  
MAINTAINER Stephane Deboudt "stephane.deboudt@mcssolutions.com"  
RUN apt-get update && apt-get install -y \  
sudo \  
pandoc \  
pandoc-citeproc \  
libcurl4-gnutls-dev \  
libcairo2-dev \  
libxt-dev \  
libssl-dev \  
libssh2-1-dev \  
libssl1.0.0  
  
# Install microbenchmark tool  
RUN R -e "install.packages(c('microbenchmark'),
repos='https://cloud.r-project.org/')"  
  
# Install Basic shiny functionality  
RUN R -e "install.packages(c('shiny', 'shinydashboard', 'shinyjs'),
repos='https://cloud.r-project.org/')"  
  
# Install dependencies of the Shiny App  
RUN R -e "install.packages(c('ggplot2', 'tidyr', 'lubridate', 'scales',
'leaflet', 'sp', 'RColorBrewer'), repos='https://cloud.r-project.org/')"  
  
# Install packages for container logging on spin-up  
RUN R -e 'install.packages("log4r")'  
  
# Install app runner  
COPY shinydockertools_0.0.1.tar.gz /root/  
RUN R CMD INSTALL /root/shinydockertools_0.0.1.tar.gz  
RUN rm /root/shinydockertools_0.0.1.tar.gz

