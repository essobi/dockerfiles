FROM rocker/hadleyverse  
  
RUN apt-get update && \  
apt-get install -y \  
mdbtools \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY r-packages.R /etc/r-packages.R  
RUN R --slave < /etc/r-packages.R  
  

