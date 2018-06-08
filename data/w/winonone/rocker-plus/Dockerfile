FROM rocker/verse:3.4.0  
  
RUN BUILD_DATE=$(TZ="America/Los_Angeles" date -I) \  
&& install2.r --error \--repos
https://mran.microsoft.com/snapshot/${BUILD_DATE} --deps TRUE \  
printr RcppArmadillo foreach matrixStats gridExtra XML \  
&& rm -rf /tmp/downloaded_packages/  
  
  
RUN r -e 'source("https://bioconductor.org/biocLite.R"); \  
biocLite("minfi"); \  
biocLite("BiocParallel");' \  
&& rm -rf /tmp/downloaded_packages/  
  
RUN r -e 'source("https://bioconductor.org/biocLite.R"); \  
biocLite("shinyMethyl"); \  
biocLite("missMethyl");' \  
&& rm -rf /tmp/downloaded_packages/  
  
  
RUN r -e 'source("https://bioconductor.org/biocLite.R"); \  
biocLite("DMRcate");'\  
&& rm -rf /tmp/downloaded_packages/

