# parent Docker  
FROM rocker/tidyverse:3.3.1  
  
  
# this is necessary for installing mzR  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libnetcdf-dev  
  
# installing necessary R packages from init  
ADD init.R /tmp/  
RUN R -f /tmp/init.R  

