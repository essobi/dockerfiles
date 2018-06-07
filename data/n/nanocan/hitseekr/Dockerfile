FROM rocker/shiny:latest  
MAINTAINER Markus List <markus.list@mpi-inf.mpg.de>  
  
#install system packages  
RUN apt-get update && apt-get install -y \  
libxml2-dev \  
redis-server \  
libcurl4-gnutls-dev \  
libssl-dev  
  
#install R packages  
ADD install.R install.R  
RUN R -e "source('install.R')"  
  
#copy shiny app to work-dir  
WORKDIR /srv/  
RUN mkdir hitseekr  
ADD . hitseekr  
  
#update shiny server conf and configure it to run hitseekr in single app mode  
RUN sed -i 's/site_dir \/srv\/shiny-server;/app_dir \/srv\/hitseekr;/g'
/etc/shiny-server/shiny-server.conf  
  
#download additional database files if needed  
WORKDIR /srv/hitseekr/  
RUN mkdir data && \  
cd data && \  
wget https://www.dropbox.com/s/to4zfhetkdofzsk/hitseekr_data.tar.gz?dl=0 && \  
tar -xzf hitseekr_data.tar.gz?dl=0 && \  
rm hitseekr_data.tar.gz?dl=0 && \  
cd .. && \  
chown -R shiny data  

