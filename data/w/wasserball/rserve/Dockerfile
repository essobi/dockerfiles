# Dotcloud ubuntu image  
FROM ubuntu:latest  
MAINTAINER wasserball  
  
# Install latest R  
RUN sudo sh -c 'echo "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/" >>
/etc/apt/sources.list'  
# add the public keys:  
RUN gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9  
RUN gpg -a --export E084DAB9 | sudo apt-key add -  
  
# Update and install  
RUN apt-get update && apt-get install -y \  
r-base \  
r-recommended \  
r-base-dev \  
libcurl4-gnutls-dev \  
libxml2-dev \  
libmime-base64-urlsafe-perl \  
libdigest-hmac-perl \  
libdigest-sha-perl \  
libssl-dev \  
libapparmor1 \  
wget  
  
# log R version  
RUN R --version  
  
#install R packages  
RUN sudo su - -c "R -e \"install.packages('Rserve',
repos='http://cran.r-project.org')\""  
RUN sudo su - -c "R -e \"install.packages('ggplot2',
repos='http://cran.r-project.org')\""  
RUN sudo su - -c "R -e \"install.packages('RJSONIO',
repos='http://cran.r-project.org')\""  
RUN sudo su - -c "R -e \"install.packages('rjson',
repos='http://cran.r-project.org')\""  
RUN sudo su - -c "R -e \"install.packages('Rmisc',
repos='http://cran.r-project.org')\""  
RUN sudo su - -c "R -e \"install.packages('signal',
repos='http://cran.r-project.org')\""  
RUN sudo su - -c "R -e \"install.packages('foreach',
repos='http://cran.r-project.org')\""  
RUN sudo su - -c "R -e \"install.packages('doParallel',
repos='http://cran.r-project.org')\""  
  
# adding start R script  
ADD start.R start.R  
ADD Rserv.conf /Rserv.conf  
EXPOSE 6311  
CMD Rscript start.R  

