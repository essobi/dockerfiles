From cablab/singleuser-julia:v4  
MAINTAINER Brockmann Consult GmbH <http://www.brockmann-consult.de>  
# Install R and R CABLAB  
USER root  
WORKDIR /srv/jupyterhub  
RUN echo "deb http://ftp5.gwdg.de/pub/misc/cran/bin/linux/debian jessie-
cran3/" >> /etc/apt/sources.list  
RUN apt-key adv --keyserver keys.gnupg.net --recv-key
6212B7B7931C4BB16280BA1306F90DE5381BA480  
RUN apt-get update  
RUN apt-get -y install libcurl4-openssl-dev libxml2-dev libxslt-dev r-base-dev  
  
RUN git clone https://github.com/CAB-LAB/RCABLAB  
RUN wget
https://cran.r-project.org/src/contrib/Archive/RNetCDF/RNetCDF_1.6.1-2.tar.gz  
RUN R CMD INSTALL RNetCDF_1.6.1-2.tar.gz  
WORKDIR /srv/jupyterhub/RCABLAB  
RUN git checkout 02998cd41ee0c3862cf698b6729471576366dd67  
RUN R CMD INSTALL RCABLAB  
WORKDIR /srv/jupyterhub  
RUN apt-get -y install libcurl4-openssl-dev libssl-dev  
RUN R -e "install.packages(c('repr', 'IRdisplay', 'crayon', 'pbdZMQ',
'devtools'),repos='http://cran.us.r-project.org');devtools::install_github('IRkernel/IRkernel');IRkernel::installspec()"  
RUN R -e
"install.packages(c('data.table'),repos='http://cran.us.r-project.org')"  
RUN R -e
"install.packages(c('ggplot2','raster','sp','zoo','rgdal','dplyr','vegan','ape','Rtsne','Rcpp','inline'),repos='http://cran.us.r-project.org')"  
  
USER jovyan  
WORKDIR /home/jovyan/work  

