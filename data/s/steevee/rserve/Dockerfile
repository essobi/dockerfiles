  
FROM ubuntu:16.04  
MAINTAINER steve@adexperiments.io  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update  
RUN apt-get update  
  
# Install packages required to install R  
RUN apt-get install -y wget sudo apt-utils  
  
# Install latest R  
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" | sudo tee -a
/etc/apt/sources.list  
RUN gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9  
RUN gpg -a --export E084DAB9 | sudo apt-key add -  
  
# Update and install R and related packages  
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
libapparmor1  
  
# log R version  
RUN R --version  
  
#install R packages  
RUN sudo su - -c "/usr/bin/R -e \"install.packages('Rserve',
repos='http://cran.r-project.org')\""  
RUN sudo su - -c "/usr/bin/R -e \"install.packages('dplyr',
repos='http://cran.r-project.org')\""  
RUN sudo su - -c "/usr/bin/R -e \"install.packages('data.table',
repos='http://cran.r-project.org')\""  
RUN sudo su - -c "/usr/bin/R -e \"install.packages('reshape2',
repos='http://cran.r-project.org')\""  
RUN sudo su - -c "/usr/bin/R -e \"install.packages('mvtnorm',
repos='http://cran.r-project.org')\""  
RUN sudo su - -c "/usr/bin/R -e \"install.packages('polycor',
repos='http://cran.r-project.org')\""  
RUN sudo su - -c "/usr/bin/R -e \"install.packages('txtplot',
repos='http://cran.r-project.org')\""  
RUN sudo su - -c "/usr/bin/R -e \"install.packages('MASS',
repos='http://cran.r-project.org')\""  
RUN sudo su - -c "/usr/bin/R -e \"install.packages('pairwiseCI',
repos='http://cran.r-project.org')\""  
RUN sudo su - -c "/usr/bin/R -e \"install.packages('devtools',
repos='http://cran.r-project.org')\""  
RUN sudo su - -c "/usr/bin/R -e \"install.packages('showtext',
repos='http://cran.r-project.org')\""  
RUN sudo su - -c "/usr/bin/R -e \"install.packages('tm',
repos='http://cran.r-project.org')\""  
RUN sudo su - -c "/usr/bin/R -e \"install.packages('wordcloud',
repos='http://cran.r-project.org')\""  
RUN sudo su - -c "/usr/bin/R -e \"install.packages('RPostgreSQL',
repos='http://cran.r-project.org')\""  
RUN sudo su - -c "/usr/bin/R -e \"install.packages('ratesci',
repos='http://cran.r-project.org')\""  
  
# adding start R script: you can find the RScript on the docker github  
ADD start.R start.R  
ADD Rserv.conf Rserv.conf  
EXPOSE 6311  
CMD Rscript start.R  

