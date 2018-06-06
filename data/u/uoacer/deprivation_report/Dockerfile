FROM rocker/geospatial:3.4.0  
RUN apt-get update && apt-get install -y libprotobuf-dev protobuf-compiler
libjq-dev  
RUN R -e "install.packages(c('highcharter', 'leaflet', 'shinycssloaders',
'shinyjs', 'tmap', 'leaflet.extras', 'plumber', 'uuid', 'curl'),
repos='https://cran.rstudio.com/');"  
RUN R -e "install.packages('GAlogger', repos =
'http://www.datatailor.be/rcube', type = 'source');"  
RUN R -e "devtools::install_github('dkahle/ggmap');"  
RUN export ADD=shiny && bash /etc/cont-init.d/add  
COPY shiny-server.conf /etc/shiny-server/shiny-server.conf  

