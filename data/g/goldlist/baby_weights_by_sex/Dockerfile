# Docker file for baby_weights_by_sex  
# Amy Goldlist, Dec, 2017  
### Note, I've based my code on Tiffany Timber's code for the
data_analysis_pipeline_eg  
# use rocker/tidyverse as the base image and  
FROM rocker/tidyverse  
  
# then install the ezknitr packages  
RUN Rscript -e "install.packages('ezknitr', repos =
'https://mran.revolutionanalytics.com/snapshot/2017-12-11')"  
  
#install stringr package  
RUN Rscript -e "install.packages('stringr', repos =
'http://cran.us.r-project.org')"  
  
#install forcats  
RUN Rscript -e "install.packages('forcats', repos =
'http://cran.us.r-project.org')"  
  
##install SDMTools  
RUN Rscript -e "install.packages('SDMTools', repos =
'http://cran.us.r-project.org')"  
  
##install scales  
RUN Rscript -e "install.packages('scales', repos =
'http://cran.us.r-project.org')"  
  
###Instal makefile2graph  
# This is based on Tiffany's docker file  
# install graphviz  
RUN apt-get install -y graphviz  
  
# install git  
RUN apt-get install -y wget  
RUN apt-get install -y make git  
  
# clone, build makefile2graph,  
# then copy key makefile2graph files to usr/bin so they will be in $PATH  
RUN git clone https://github.com/lindenb/makefile2graph.git  
  
RUN make -C makefile2graph/.  
  
RUN cp makefile2graph/makefile2graph usr/bin  
RUN cp makefile2graph/make2graph usr/bin  

