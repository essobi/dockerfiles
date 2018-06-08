FROM rocker/shiny:latest  
  
# Installing packages needed for check traffic on the container and kill if
none  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup && \  
echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache && \  
apt-get -qq update && apt-get install --no-install-recommends -y net-tools
procps libgdal-dev libproj-dev && \  
# Installing R package dedicated to the shniy app  
Rscript -e "install.packages('leaflet')" && \  
Rscript -e "install.packages('ggvis')" && \  
Rscript -e "install.packages('dplyr')" && \  
Rscript -e "install.packages('RColorBrewer')" && \  
Rscript -e "install.packages('raster')" && \  
Rscript -e "install.packages('gstat')" && \  
Rscript -e "install.packages('rgdal')" && \  
Rscript -e "install.packages('Cairo')" && \  
Rscript -e "install.packages('shinyjs')" && \  
Rscript -e "install.packages('shinydashboard')"  
# Bash script to check traffic  
COPY SIG /srv/shiny-server/sample-apps/SIG/  
ADD ./monitor_traffic.sh /monitor_traffic.sh  
COPY shiny-server.sh /usr/bin/shiny-server.sh  
CMD ["/usr/bin/shiny-server.sh"]  

