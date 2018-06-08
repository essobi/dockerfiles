FROM channing/r-base  
  
MAINTAINER Marcia Goetsch "marcia.goetsch@channing.harvard.edu"  
# Download and install shiny server  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
gdebi-core \  
pandoc  
  
RUN R -e "install.packages(c('shiny'), repos='https://cran.rstudio.com/')"  
  
RUN wget https://download3.rstudio.org/ubuntu-12.04/x86_64/shiny-
server-1.5.0.730-amd64.deb \  
&& gdebi --n shiny-server-1.5.0.730-amd64.deb \  
&& rm shiny-server-1.5.0.730-amd64.deb \  
&& mkdir -p /srv/shiny-server \  
&& cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/ \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN R -e "install.packages(c('rmarkdown'), repos='https://cran.rstudio.com/')"  
  
COPY shiny-server.sh /usr/bin/shiny-server.sh  
  
EXPOSE 3838  
CMD ["/usr/bin/shiny-server.sh"]  

