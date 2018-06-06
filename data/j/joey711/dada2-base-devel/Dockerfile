FROM bioconductor/release_core2  
  
LABEL project="dada2"  
  
MAINTAINER Paul McMurdie "paul.mcmurdie@wholebiome.com"  
# Execute dependency installation script for build  
COPY install.R /tmp/  
RUN R -f /tmp/install.R  
RUN R -e "packageVersion('dada2')"  
  
CMD ["R"]  

