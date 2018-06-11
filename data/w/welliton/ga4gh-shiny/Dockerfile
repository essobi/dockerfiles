# welliton/ga4gh-shiny  
FROM rocker/shiny  
  
MAINTAINER Welliton Souza "well309@gmail.com"  
COPY install.R /tmp/install.R  
  
RUN apt-get update && \  
apt-get install --yes --no-install-recommends libssl-dev libxml2-dev && \  
R -f /tmp/install.R && \  
rm -rf /var/lib/apt/lists/* /tmp/install.R /srv/shiny-server/*  
  
COPY docker-ga4gh-shiny-entrypoint /usr/local/bin/  
  
ENTRYPOINT ["docker-ga4gh-shiny-entrypoint"]  
  
CMD ["/usr/bin/shiny-server.sh"]

