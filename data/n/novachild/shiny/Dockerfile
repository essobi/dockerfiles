FROM novachild/shinybase:latest  
#Modified from rocker/shiny image on DockerHub  
#MAINTAINER Winston Chang "winston@rstudio.com"  
MAINTAINER David Griswold "davidgriswold@cpm.org"  
#This very simple image only copies the apps over, so that rebuilding this
image won't require a complete redownload and rebuild of all libraries and
server  
COPY apps /srv/shiny-server  
RUN chmod -R a+rw /srv/shiny-server  

