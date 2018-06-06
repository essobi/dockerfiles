FROM ubuntu:14.04.3  
MAINTAINER cannin  
  
# UBUNTU  
## Update Ubuntu and add extra repositories  
RUN apt-get -y install software-properties-common  
RUN apt-add-repository -y ppa:marutter/rrutter  
RUN apt-get -y update && apt-get -y upgrade  
  
# Install basic commands  
RUN apt-get -y install links nano telnet  
RUN apt-get -y install libcurl4-openssl-dev  
  
# Necessary for getting the latest R version  
RUN apt-get -y install r-base r-base-dev  
  
# Install Rserve and common R packages  
RUN R -e "install.packages(c('Rserve', 'RCurl', 'plyr', 'digest', 'ggplot2',
'colorspace', 'stringr', 'RColorBrewer', 'reshape2', 'scales', 'proto',
'dichromat', 'bitops', 'gtable', 'Rcpp'), repos='http://cran.rstudio.com/')"  
# adding start R script: you can find the RScript on the docker github  
ADD start.R /start.R  
ADD Rserve.conf /etc/Rserve.conf  
  
EXPOSE 6311  
  
CMD Rscript start.R  

