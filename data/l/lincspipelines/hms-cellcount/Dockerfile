FROM rocker/rstudio-stable:3.4.0  
COPY ./Level2_to_Level3_and4.R /home/rstudio/  
  
RUN apt-get update -qq && \  
apt-get install -y \  
zlib1g-dev \  
libssh2-1-dev \  
libxml2-dev \  
curl \  
libpng-dev \  
sudo \  
wget  
  
RUN R -e "source('https://bioconductor.org/biocLite.R'); biocLite('GRmetrics',
ask=FALSE, siteRepos='https://mran.microsoft.com/snapshot/2017-11-01');"  
RUN R -e "install.packages('ghit', repos =
'https://mran.microsoft.com/snapshot/2017-11-01')"  
RUN R -e "install.packages('readr', repos =
'https://mran.microsoft.com/snapshot/2017-11-01')"  
RUN R -e
"ghit::install_github('schurerlab/LINCSDataPortal@3680b4dc2d6b5af192f49987eda96ee477da334a')"  

