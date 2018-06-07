FROM r-base:latest  
  
MAINTAINER "Ben J. Ward <axolotlfan9250@gmail.com>"  
RUN R -e "install.packages(c('ggplot2', 'png', 'grid', 'gridExtra', 'ape'))"  
  
RUN R -e "source('http://bioconductor.org/biocLite.R'); biocLite();
biocLite('Biostrings', 'IRanges')"  
  
COPY HybridCheck_1.0.tar.gz /  
  
RUN R CMD INSTALL /HybridCheck_1.0.tar.gz  
  
CMD ["R"]  

