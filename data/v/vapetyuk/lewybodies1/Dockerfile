  
# parent Docker  
FROM rocker/verse:3.3.2  
  
# this is necessary for installing mzR and nloptr  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libnetcdf-dev \  
libnlopt-dev # NLopt library  
  
# FreeTDS  
RUN apt-get install -y --no-install-recommends \  
unixodbc unixodbc-dev freetds-dev freetds-bin tdsodbc  
  
# CIFS for accessing files on Windows shares  
RUN apt-get install -y --no-install-recommends \  
cifs-utils  
  
# later the installation of bnlearn will be moved to init.R  
# RUN wget
http://cran.r-project.org/src/contrib/Archive/bnlearn/bnlearn_3.9.tar.gz  
# RUN R CMD INSTALL bnlearn_3.9.tar.gz  
# installing necessary R packages from init  
ADD init.R /tmp/  
RUN R -f /tmp/init.R  
  
# bumping up rstudio user to sudoer just in case  
# RUN useradd -m rstudio --groups sudo # failed  
RUN usermod -a -G sudo rstudio  

