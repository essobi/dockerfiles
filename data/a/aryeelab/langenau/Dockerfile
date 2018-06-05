FROM rocker/shiny  
  
RUN apt-get update && \  
apt-get install -y git libxml2-dev libssl-dev ghostscript  
  
# Install langenau  
COPY . /srv/shiny-server/langenau  
  
WORKDIR /srv/shiny-server/langenau  
  
# Install packrat packages  
RUN Rscript -e 'install.packages("packrat"); \  
packrat::restore()'  
  
# Temporary permissions hack  
RUN chown shiny:shiny -R packrat && \  
chown shiny:shiny .gitignore  
  
# Serve only the langenau app (replace /srv/shiny-server with /srv/shiny-
server/langenau)  
RUN sed -i 's/\/srv\/shiny-server/\/srv\/shiny-server\/langenau/' /etc/shiny-
server/shiny-server.conf  
  
# Improve first page load time by not shutting down the R session when idle  
RUN sed -i '/location \/ {/a app_idle_timeout 0;' /etc/shiny-server/shiny-
server.conf  
  
# Increase app load timeout  
RUN sed -i '/location \/ {/a app_init_timeout 60;' /etc/shiny-server/shiny-
server.conf  
  
# Add Google Analytics tracking code  
# RUN sed -i '/location \/ {/a google_analytics_id UA-37764824-4;' /etc/shiny-
server/shiny-server.conf  
# Start and expose shiny server  
EXPOSE 3838  
CMD /usr/bin/shiny-server.sh  
  

