FROM inwt/r-base:3.4.4  
  
RUN apt-get -y update \  
&& apt-get install -y --no-install-recommends \  
default-jdk \  
libbz2-dev \  
liblzma-dev \  
libpcre3-dev \  
libmariadb-client-lgpl-dev \  
&& apt-get autoremove -y \  
&& apt-get autoclean -y \  
&& install2.r \  
dplyr \  
data.table \  
futile.logger \  
gbm \  
ggplot2 \  
gridExtra \  
lme4 \  
mgcv \  
rJava \  
RMySQL \  
tidyr \  
&& installGithub \  
INWT/dbtools \  
INWT/mctools \  
&& rm -rf /tmp/downloaded_packages/*  

