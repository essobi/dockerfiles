FROM rocker/hadleyverse:latest  
  
# rstudio + shiny + hadleyverse R packages  
# For details and usage see  
# https://github.com/skranz/shinyrstudioDocker  
MAINTAINER Sebastian Kranz "sebastian.kranz@uni-ulm.de"  
#RUN su - -c "R -e \"install.packages('shiny',
repos='https://cran.rstudio.com/')\""  
RUN apt-get update && \  
apt-get install -y gdebi-core  
RUN wget\  
https://raw.github.com/rstudio/shiny-server/master/config/upstart/shiny-
server.conf\  
-O /etc/init/shiny-server.conf  
  
RUN wget https://download3.rstudio.org/ubuntu-12.04/x86_64/shiny-
server-1.4.7.815-amd64.deb  
RUN gdebi -n shiny-server-1.4.7.815-amd64.deb  
  
EXPOSE 3838  
# The rocker/rstudio image uses the s6 init system  
# Copy run-shiny.sh to the right location to start up the shiny server  
RUN mkdir -p /etc/services.d/shiny-server  
COPY run-shiny.sh /etc/services.d/shiny-server/run  
  
# Copy modified userconf.sh  
COPY run-rstudio.sh /etc/services.d/rstudio/run  
COPY userconf.sh /etc/cont-init.d/conf  
  
CMD ["/init"]  
  
# docker build -t "shinyrstudio:latest" .

