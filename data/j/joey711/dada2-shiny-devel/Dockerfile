FROM rocker/shiny  
  
LABEL project="dada2"  
LABEL application="dada2GUI"  
  
MAINTAINER Paul McMurdie "paul.mcmurdie@wholebiome.com"  
## dependencies. Use cloudfront, official CDN gives frequent 503 errors  
RUN sed -i "s/deb.debian.org/cdn-fastly.deb.debian.org/" /etc/apt/sources.list
\  
&& sed -i "s/security.debian.org/cdn-fastly.debian.org\/debian-security/"
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
libssl-dev  
  
# Install Bioconductor basic  
COPY install-bioc.R /tmp/  
RUN R -f /tmp/install-bioc.R  
# Install DADA2  
COPY install.R /tmp/  
RUN R -f /tmp/install.R  
RUN R -e "packageVersion('dada2')"  
RUN cp -R /usr/local/lib/R/site-library/dada2/shiny /srv/shiny-server/dada2  
  
EXPOSE 3838  
CMD ["/usr/bin/shiny-server.sh"]  

