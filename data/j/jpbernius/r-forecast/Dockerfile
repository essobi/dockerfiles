FROM r-base  
MAINTAINER Jan Philip Bernius <janphilip@bernius.net>  
  
# Install R packages  
ADD install-packages.R install-packages.R  
RUN Rscript install-packages.R  
  
# Load forecast Package on startup  
ENV R_DEFAULT_PACKAGES 'forecast'  
CMD R  

