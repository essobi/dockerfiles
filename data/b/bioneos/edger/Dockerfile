# Base image from Ubuntu #  
FROM r-base:3.4.2  
LABEL base.image="r-base:3.4.2"  
LABEL software="R with edgeR analysis library"  
LABEL software.version="3.20.2"  
LABEL maintainer="Mike Smith <msmith@bioneos.com>"  
  
USER root  
  
# R is already installed and ready, install the edgeR package and the
dependencies  
WORKDIR /tmp  
RUN wget
https://github.com/bioneos/images/raw/master/edgeR/src/edgeR_3.20.2.tar.gz &&
\  
tar zxvf edgeR_3.20.2.tar.gz  
RUN wget
https://github.com/bioneos/images/raw/master/edgeR/src/limma_3.34.4.tar.gz &&
\  
tar zxvf limma_3.34.4.tar.gz  
RUN wget
https://github.com/bioneos/images/raw/master/edgeR/src/locfit_1.5-9.1.tar.gz
&& \  
tar zxvf locfit_1.5-9.1.tar.gz  
RUN wget
https://github.com/bioneos/images/raw/master/edgeR/src/Rcpp_0.12.14.tar.gz &&
\  
tar zxvf Rcpp_0.12.14.tar.gz  
  
RUN R -e "install.packages(c('/tmp/limma', '/tmp/locfit', '/tmp/Rcpp',
'/tmp/edgeR'), repos = NULL, type = 'source')"  
  
# Default command  
CMD /bin/bash  

