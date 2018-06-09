FROM rocker/shiny  
  
MAINTAINER "Nicholas Heyek and David LeBauer"  
  
ENV bety_dbname=bety  
ENV bety_password=bety  
ENV bety_host=localhost  
ENV bety_user=bety  
ENV bety_port=5432  
  
RUN apt-get update -qq \  
&& apt-get -y install --no-install-recommends \  
cron \  
libgeos-dev \  
libpq-dev \  
&& install2.r --error \  
cronR \  
dbplyr \  
dplyr \  
ggplot2 \  
leaflet \  
lubridate \  
shiny \  
shinythemes \  
rgeos \  
RPostgreSQL \  
timevis \  
&& rm -rf /srv/shiny-server/sample-apps  
  
COPY . /srv/shiny-server/  
COPY shiny-server.conf /etc/shiny-server/  
RUN chown -R shiny:shiny /srv/shiny-server && \  
chown -R shiny:shiny /var/lib/shiny-server  
USER shiny  

