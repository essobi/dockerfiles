# Docker file for ramen-vs-pho  
# Jill Cates, Dec 2017  
# use tidyverse as base docker img  
FROM rocker/tidyverse  
  
# install the package dependecies  
RUN Rscript -e "install.packages('ezknitr', repos =
'https://mran.revolutionanalytics.com/snapshot/2017-12-11')"  
RUN Rscript -e "install.packages('packrat', repos =
'http://cran.us.r-project.org')"  
RUN Rscript -e "install.packages('maps', repos =
'http://cran.us.r-project.org')"  
RUN Rscript -e "install.packages('RColorBrewer', repos =
'http://cran.us.r-project.org')"  
RUN Rscript -e "install.packages('forcats', repos =
'http://cran.us.r-project.org')"  
RUN Rscript -e "install.packages('reshape2', repos =
'http://cran.us.r-project.org')"  
RUN Rscript -e "install.packages('readr', repos =
'http://cran.us.r-project.org')"  
  
# install python 3  
RUN apt-get update \  
&& apt-get install -y python3-pip python3-dev \  
&& cd /usr/local/bin \  
&& ln -s /usr/bin/python3 python \  
&& pip3 install --upgrade pip  
  
# get python package dependencies  
RUN apt-get install -y python3-tk  

