FROM skranz/rskranz:latest  
  
# based on skranz/shinyrstudio  
# so we already have  
# rstudio + shiny + hadleyverse R packages  
# rskranz installs several additional packages  
MAINTAINER Sebastian Kranz "sebastian.kranz@uni-ulm.de"  
# install and start cron  
RUN apt-get update && apt-get install -y cron  
COPY start_cron.sh /etc/cont-init.d/start_cron.sh  
  
# copy and run package installation file  
COPY install.r /tmp/install.r  
RUN Rscript /tmp/install.r  
  
COPY install2.r /tmp/install2.r  
RUN Rscript /tmp/install2.r  
  
# Use manual shiny-server configuration  
COPY shiny-server.conf /etc/shiny-server/shiny-server.conf  
RUN chmod 644 /etc/shiny-server/shiny-server.conf  

