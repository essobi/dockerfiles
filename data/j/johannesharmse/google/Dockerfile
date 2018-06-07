# Docker file for Google_Location_Analysis  
# Johannes Harmse  
# Date Created: 16-12-2017  
# Last modified: 17-12-2017  
# Description  
#  
# The purpose of the Dockerfile is to create a light-weight  
# virtual environment to run the Google analysis.  
#  
# A debian environment is created which hosts base R.  
# Packrat is used for package dependencies.  
# Bash is used to run commands as default  
# use rocker:r-base as base image  
FROM rocker/r-base  
  
# get OS updates and install build tools  
RUN apt-get update  
RUN apt-get install -y build-essential  
  
# install wget and git  
RUN apt-get install -y wget  
RUN apt-get install -y make git  
  
# clone, build Google-Data-Analysis  
RUN git clone https://github.com/johannesharmse/Google-Data-Analysis.git  
  
# install necessary software. Use yes, to automatically agree to installation  
RUN yes | apt-get install aptitude  
RUN yes | apt-get install libcurl4-openssl-dev  
RUN yes | apt-get install libxml2-dev  
RUN yes | apt-get install libssl-dev/unstable  
RUN yes | apt-get install pandoc  
  
# change Rprofile to accommodate packrat  
RUN export R_PROFILE=/Google-Data-Analysis/.Rprofile  
  
# change working directory to accommodate analysis scripts  
WORKDIR "/Google-Data-Analysis"  
  
# install and activate packrat  
RUN R -e 'install.packages("packrat")'  
RUN R -e 'packrat::restore()'  
RUN R -e 'packrat::on()'  
  
# Set the default command  
ENTRYPOINT ["bash"]  

