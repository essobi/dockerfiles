FROM ubuntu:14.04  
  
##RUN sh -c 'echo "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/" >>
/etc/apt/sources.list'  
##RUN gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9  
##RUN gpg -a --export E084DAB9 | sudo apt-key add -  
##RUN apt-get update  
##RUN apt-get -y install r-base  
RUN apt-get update  
RUN apt-get install -y git  
  
CMD git clone https://github.com/brianmoranOK/rocker2.git /rocker2/  
  
##CMD cd rocker2  
  
##CMD Rscript mlb-analytics-engine.R

