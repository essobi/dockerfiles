FROM bioconductor/release_core2:R3.5.0_Bioc3.7  
  
# basic packages  
RUN Rscript -e
"install.packages(c('dplyr','Hmisc','phangorn','reshape2','tidyverse'))"  
  
# bio packages  
RUN Rscript -e "source('https://bioconductor.org/biocLite.R');
biocLite(c('dada2','DECIPHER','DESeq2','edgeR','msa','phyloseq'))"  

