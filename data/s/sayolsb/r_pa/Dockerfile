FROM r-base  
RUN apt-get update  
RUN apt-get install -y libcurl4-gnutls-dev libxml2-dev  
RUN Rscript -e
'install.packages(c("Hmisc","data.table","parallel","matrixStats","ggplot2","proto"))'  

