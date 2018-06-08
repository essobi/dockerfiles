FROM rocker/shiny:latest  
#modified from rocker/shiny image on DockerHub  
#MAINTAINER Winston Chang "winston@rstudio.com"  
MAINTAINER David Griswold "davidgriswold@cpm.org"  
COPY sources.list /etc/apt/  
  
#Add some fonts  
RUN apt-get update && apt-get install -y -t unstable \  
fonts-freefont-ttf \  
fonts-liberation \  
libxml2-dev \  
libssl-dev  
  
#Including the MS ones to get Times New Roman  
RUN yes | apt-get install -y ttf-mscorefonts-installer  
  
#But seriously, webdings? Kill that.  
RUN rm /usr/share/fonts/truetype/msttcorefonts/*ebdings.ttf  
  
#Get a better pandoc than the one included  
RUN wget
https://github.com/jgm/pandoc/releases/download/1.19.2.1/pandoc-1.19.2.1-1-amd64.deb  
RUN dpkg --force-all -i ./pandoc-1.19.2.1-1-amd64.deb  
  
# Shiny server should already be installed, so only need to add libraries  
RUN R -e "install.packages(c('devEMF','googleAuthR','dplyr',
'diagram','pander', 'xtable','plyr','reshape','scales','colourpicker','shiny',
'rmarkdown','ggplot2','latex2exp','Cairo','cowplot','shinyjs','gridExtra','RColorBrewer','randomNames'),
repos='https://cran.rstudio.com/')" && \  
chmod a+rx -R /srv/shiny-server && \  
chmod a+rw -R /usr/local/lib/R/site-library  
  
#Exppose port 3838 and start the server  
EXPOSE 3838  
COPY shiny-server.sh /usr/bin/shiny-server.sh  
  
CMD ["/usr/bin/shiny-server.sh"]  

