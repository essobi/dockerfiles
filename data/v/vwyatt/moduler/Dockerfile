############################################################  
# Dockerfile to build fruadscore container images  
# Based on Ubuntu  
############################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu:trusty  
  
# File Author / Maintainer  
MAINTAINER Socure "support@socure.me"  
  
################## BEGIN INSTALLATION ######################  
RUN apt-get update  
  
  
# Install RApache module  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository ppa:opencpu/rapache  
RUN apt-get update  
RUN apt-get install -y --force-yes libapache2-mod-r-base  
  
# Install Apache web server  
RUN apt-get install -y apache2  
  
# Install R packages  
RUN Rscript -e 'install.packages("futile.logger",
repo="http://cran.rstudio.com/")'  
RUN Rscript -e 'install.packages("rjson", repo="http://cran.rstudio.com/")'  
RUN Rscript -e 'install.packages("Rook", repo="http://cran.rstudio.com/")'  
  
# Remove redundant configuration  
RUN rm /etc/apache2/mods-enabled/mpm_event.conf  
RUN rm /etc/apache2/mods-enabled/mpm_event.load  
RUN rm /etc/apache2/mods-enabled/mod_R.load  
RUN rm /etc/apache2/sites-enabled/*  
  
# Copy config files into image  
ADD src/predict.R /opt/webservice/  
ADD src/RSourceOnStartup.R /opt/webservice/  
ADD conf/rapache.conf /opt/webservice/  
ADD conf/predict.logrotate /etc/logrotate.d/  
ADD model /opt/webservice/model/  
  
# Link to new config  
RUN ln -s /opt/webservice/rapache.conf /etc/apache2/sites-enabled/  
  
  
################## END INSTALLATION ######################  
# Expose the default port  
EXPOSE 80  
  
# Set default container command  
CMD ["-D", "FOREGROUND"]  
ENTRYPOINT ["/usr/sbin/apachectl"]  
  
  

