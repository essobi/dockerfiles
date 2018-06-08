FROM ubuntu:latest  
MAINTAINER Andres Herrera - Mario Castillo
"fabio.herrera@correounivalle.edu.co - mario.castillo@correounivalle.edu.co"  
RUN apt-get update -y  
RUN apt-get install software-properties-common -y  
RUN apt-get install python-software-properties -y  
RUN add-apt-repository "ppa:marutter/rrutter" -y  
RUN add-apt-repository "ppa:marutter/c2d4u" -y  
RUN add-apt-repository "ppa:ubuntugis/ubuntugis-unstable" -y  
RUN apt-get update -y  
RUN apt-get install libgdal-dev libgeos-dev libproj-dev libudunits2-dev
liblwgeom-dev r-base r-cran-readr vim procps git -y  
RUN R -e "install.packages(c('raster')
,repos='https://cloud.r-project.org/',dependencies=TRUE)"  
RUN R -e "install.packages(c('rgeos')
,repos='https://cloud.r-project.org/',dependencies=TRUE)"  
RUN R -e "install.packages(c('rgdal')
,repos='https://cloud.r-project.org/',dependencies=TRUE)"  
  

