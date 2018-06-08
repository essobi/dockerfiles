# Docker file for LosAngeles  
# Tariq Hassan, Dec, 2017  
#  
# Usage:  
#  
# To build the docker image use:  
#  
# docker build --tag thass/losangeles .  
# use rocker/tidyverse as the base image and  
FROM rocker/tidyverse  
  
# Install R packages generally  
# (although note that packrat will restore packages needed by my single R
script: `src/visualization/visualize.R`).  
RUN Rscript -e "install.packages('ezknitr', repos =
'https://mran.revolutionanalytics.com/snapshot/2017-12-11')"  
RUN Rscript -e "install.packages('packrat', repos =
'http://cran.us.r-project.org')"  
RUN Rscript -e "install.packages('grid', repos =
'http://cran.us.r-project.org')"  
RUN Rscript -e "install.packages('ggmap', repos =
'http://cran.us.r-project.org')"  
RUN Rscript -e "install.packages('magick', repos =
'http://cran.us.r-project.org')"  
RUN Rscript -e "install.packages('scales', repos =
'http://cran.us.r-project.org')"  
RUN Rscript -e "install.packages('forcasts', repos =
'http://cran.us.r-project.org')"  
RUN Rscript -e "install.packages('cowplot', repos =
'http://cran.us.r-project.org')"  
RUN Rscript -e "install.packages('ggthemes', repos =
'http://cran.us.r-project.org')"  
RUN Rscript -e "install.packages('tidyverse', repos =
'http://cran.us.r-project.org')"  
RUN Rscript -e "install.packages('optparse', repos =
'http://cran.us.r-project.org')"  
RUN Rscript -e "install.packages('packrat', repos =
'http://cran.us.r-project.org')"  
RUN Rscript -e "install.packages('packrat', repos =
'http://cran.us.r-project.org')"  
RUN Rscript -e "install.packages('ezknitr', version = '0.6', repos =
'http://cran.us.r-project.org')"  
  
# install python 3  
RUN apt-get update \  
&& apt-get install -y python3-pip python3-dev \  
&& cd /usr/local/bin \  
&& ln -s /usr/bin/python3 python \  
&& pip3 install --upgrade pip  
  
# Insall JPEG library needed for R's JPEG package  
RUN apt-get install -y libjpeg-dev  
  
# Install ImageMagick for R's Magick  
RUN apt-get install -y gcc  
RUN apt-get install -y imagemagick  
RUN apt-get install -y libmagick++-dev  
  
# get python package dependencies  
RUN apt-get install -y python3-tk  
  
COPY requirements.txt ./  
RUN pip3 install --no-cache-dir -r requirements.txt  
  
RUN apt-get update && \  
pip3 install pandas && \  
rm -rf /var/lib/apt/lists/*  

