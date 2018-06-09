# Docker file for student_performance_predictions  
# Amy Goldlist, January 2018  
# use rocker/tidyverse as the base image and  
FROM rocker/tidyverse  
  
  
  
#install cowplot package  
RUN Rscript -e "install.packages('cowplot', repos =
'http://cran.us.r-project.org')"  
  
# install git  
RUN apt-get install -y wget  
RUN apt-get install -y make git  
  
###I've looked at Tiffany's data analysis pipeline from class last term for
inspiration  
# install python 3  
RUN apt-get update \  
&& apt-get install -y python3-pip python3-dev \  
&& cd /usr/local/bin \  
&& ln -s /usr/bin/python3 python \  
&& pip3 install --upgrade pip  
  
# get python package dependencies  
RUN apt-get install -y python3-tk  
  
# install numpy  
RUN pip3 install numpy  
  
## install pandas  
RUN pip3 install pandas  
  
##install scipy  
RUN pip3 install scipy  
  
##install sklearn  
RUN pip3 install sklearn  

