FROM stefanfritsch/shiny_statup  
MAINTAINER Stefan Fritsch <stefan.fritsch@stat-up.com>  
  
RUN apt-get update  
# RUN apt-get -o Dpkg::Options::="--force-confold" install -y libssl-dev apt-
utils libxml2-dev libgdal-dev libudunits2-dev  
# paralleles kompilieren von Paketen  
RUN sed -i "s/^MAKE=.*$/MAKE='make -j 6'/g" /usr/lib/R/etc/Renviron  
  
RUN apt-get clean  
  
USER shiny  
  
COPY global.r /home/shiny/global.r  
RUN mkdir /home/shiny/.checkpoint  
  
RUN Rscript ~/global.r  
  
USER root  
  
RUN mkdir /var/lib/shiny-server/bookmarks  
RUN chown shiny: /var/lib/shiny-server/bookmarks  
  
# RUN sed -i "s#server {#server {\n sanitize_errors off;\n disable_protocols
xdr-streaming xhr-streaming iframe-eventsource iframe-htmlfile;#" /etc/shiny-
server/shiny-server.conf  
# USER shiny  
  
EXPOSE 3838  
CMD ["/usr/bin/shiny-server.sh"]  

