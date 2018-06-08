FROM rocker/shiny:latest  
  
# Installing packages needed for check traffic on the container and kill if
none  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup && \  
echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache && \  
apt-get -qq update && apt-get install --no-install-recommends -y net-tools
procps && \  
# Installing R package dedicated to the shniy app  
Rscript -e "install.packages('leaflet')"  
# Bash script to check traffic  
COPY SIG /srv/shiny-server/sample-apps/SIG  
ADD ./monitor_traffic.sh /monitor_traffic.sh  
COPY shiny-server.sh /usr/bin/shiny-server.sh  
CMD ["/usr/bin/shiny-server.sh"]  

