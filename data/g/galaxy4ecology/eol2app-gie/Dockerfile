FROM rocker/shiny:latest  
  
# Installing packages needed for check traffic on the container and kill if
none  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup && \  
echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache && \  
apt-get -qq update && apt-get install --no-install-recommends -y net-tools
procps  
  
# Bash script to check traffic  
COPY CEFE /srv/shiny-server/sample-apps/CEFE  
ADD ./monitor_traffic.sh /monitor_traffic.sh  
COPY shiny-server.sh /usr/bin/shiny-server.sh  
CMD ["/usr/bin/shiny-server.sh"]  

