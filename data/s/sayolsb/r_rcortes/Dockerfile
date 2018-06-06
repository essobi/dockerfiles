FROM r-base  
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R");
biocLite("impute");'  
RUN Rscript -e
'install.packages(c("Hmisc","compareGroups","PMA","CCA","ggplot2","GGally","CNVassoc"))'  

