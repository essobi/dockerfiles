FROM ubuntu:14.04  
MAINTAINER <support@collectiveacuity.com>  
  
# Update Ubuntu Environment  
RUN apt-get update  
RUN apt-get --fix-missing install -y python  
  
# Install R-Base  
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/" >>
/etc/apt/sources.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9  
RUN apt-get update  
RUN apt-get install -y r-base  
  
# Install RblpAPI Dependencies  
RUN echo 'options(repos = c(CRAN = "https://cran.rstudio.com/"),
download.file.method = "libcurl")' >> /etc/R/Rprofile.site  
RUN Rscript -e 'install.packages("BH",dependencies=TRUE)'  
RUN Rscript -e 'install.packages("Rcpp",dependencies=TRUE)'  
  
# Install RblpAPI  
RUN Rscript -e 'install.packages("Rblpapi",dependencies=TRUE)'  
  
# Documentation  
# http://cran.stat.ucla.edu/  
# https://github.com/Rblp/Rblpapi  
# https://hub.docker.com/r/dmccloskey/r-base/~/dockerfile/  

