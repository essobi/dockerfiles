FROM rocker/tidyverse  
  
# News: Base now on rocker/rstudio since shiny is now supported  
# based on skranz/shinyrstudio  
# so we already have  
# rstudio + shiny + tidverse R packages  
MAINTAINER Sebastian Kranz "sebastian.kranz@uni-ulm.de"  
## running with "-e ADD=shiny" adds shiny server  
COPY add_shiny.sh /etc/cont-init.d/add  
  
RUN export ADD=shiny && bash /etc/cont-init.d/add  
  
# Use manual shiny-server configuration  
COPY shiny-server.conf /etc/shiny-server/shiny-server.conf  
RUN chmod 644 /etc/shiny-server/shiny-server.conf  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libv8-3.14-dev  
COPY install.r /tmp/install.r  
RUN Rscript /tmp/install.r  

