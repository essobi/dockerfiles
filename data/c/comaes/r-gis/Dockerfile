FROM comaes/r-base  
  
#install required system libraries ("unstable" tag refers to the debian base
image for which some libraries  
# are marked as unstable at the time of creation of this file)  
RUN apt-get update  
RUN apt-get install -y -q -t unstable libgeos++-dev \  
libgeos-3.5.1 \  
libgeos-c1v5 \  
libgeos-dbg \  
libgeos-dev \  
libgdal-dev \  
libproj-dev \  
libgeos-doc  
  
#install R dependencies  
RUN R -e "install.packages('maptools', repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages('ggmap', repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages('ggplot2', repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages('leaflet', repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages('rgdal', repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages('raster', repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages('rgeos', repos='http://cran.rstudio.com/')"  
  
#run server  
CMD ["/usr/bin/shiny-server.sh"]  

