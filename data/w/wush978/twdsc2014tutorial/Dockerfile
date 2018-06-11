#  
# bridgewell dockerfile template  
#  
# Pull base image.  
FROM rocker/rstudio  
MAINTAINER Wush Wu  
  
USER root  
  
RUN apt-get update && apt-get install -y libcurl4-openssl-dev libxml2-dev  
  
# install required packages  
RUN Rscript -e "install.packages('DSC2014Tutorial', repo =
c('http://taiwanrusergroup.github.io/R', 'http://cran.csie.ntu.edu.tw'), type
= 'source')"  
RUN adduser --disabled-password --gecos "" guest  
RUN echo "guest:guest" | chpasswd  
EXPOSE 8787  

