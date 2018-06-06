FROM bioconductor/release_core2  
  
LABEL project="dada2"  
LABEL version="release"  
  
MAINTAINER Paul McMurdie "paul.mcmurdie@wholebiome.com"  
RUN R -e 'source("https://bioconductor.org/biocLite.R"); biocLite("dada2")'  
  
CMD ["R"]  

