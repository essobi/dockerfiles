FROM achubaty/r-spatial-base  
MAINTAINER Tesera Systems Inc.  
  
RUN apt-get update && apt-get -y dist-upgrade  
  
ENV KTPIPATH /opt/ktpi  
WORKDIR $KTPIPATH  
  
# Install R packages  
RUN R -e 'install.packages(c("raster"))'  
RUN mkdir -p /opt/ktpi  
  
COPY R/* /opt/ktpi/  
  
CMD ["/bin/bash"]  

