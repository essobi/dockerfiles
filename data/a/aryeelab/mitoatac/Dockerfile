FROM rocker/shiny  
  
RUN rm /var/lib/apt/lists/*dists* && \  
apt-get update && \  
apt-get install -y git libxml2-dev libssl-dev ghostscript  
  
# Install mitoATAC  
COPY . /srv/shiny-server/mitoATAC  
  
WORKDIR /srv/shiny-server/mitoATAC  
  
# Install packrat packages  
RUN Rscript -e 'install.packages("packrat"); \  
packrat::restore()'  
  
# Temporary permissions hack  
RUN chown shiny:shiny -R packrat && \  
chown shiny:shiny .gitignore  
  
# Serve only the mitoATAC app (replace /srv/shiny-server with /srv/shiny-
server/mitoATAC)  
RUN sed -i 's/\/srv\/shiny-server/\/srv\/shiny-server\/mitoATAC/' /etc/shiny-
server/shiny-server.conf  
  
# Improve first page load time by not shutting down the R session when idle  
RUN sed -i '/location \/ {/a app_idle_timeout 0;' /etc/shiny-server/shiny-
server.conf  
  
# Increase app load timeout  
RUN sed -i '/location \/ {/a app_init_timeout 60;' /etc/shiny-server/shiny-
server.conf  
  
# Start and expose shiny server  
EXPOSE 3838  
CMD /usr/bin/shiny-server.sh  

