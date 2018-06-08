# Docker file for mentalhealth_project  
# Abishek Murali, Dec, 2017  
# use rocker/tidyverse as the base image and  
FROM r-base  
  
# then install the ezknitr packages  
RUN Rscript -e "install.packages('ezknitr', repos =
'https://mran.revolutionanalytics.com/snapshot/2017-12-11')"  
# install python 3  
RUN apt-get update \  
&& apt-get install -y python3-pip python3-dev \  
&& cd /usr/local/bin \  
&& ln -s /usr/bin/python3 python \  
&& pip3 install --upgrade pip  
  
# get python package dependencies  
RUN apt-get install -y python3-tk  
  
RUN apt-get update && \  
pip3 install pandas && \  
rm -rf /var/lib/apt/lists/*  
RUN apt-get update && \  
pip3 install numpy && \  
rm -rf /var/lib/apt/lists/*  
RUN apt-get update && \  
pip3 install matplotlib && \  
rm -rf /var/lib/apt/lists/*  
RUN apt-get update && \  
pip3 install seaborn && \  
rm -rf /var/lib/apt/lists/*  

