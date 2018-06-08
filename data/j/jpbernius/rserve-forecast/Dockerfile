FROM r-base  
MAINTAINER Jan Philip Bernius <janphilip@bernius.net>  
  
# Install R packages  
ADD install-packages.R install-packages.R  
RUN Rscript install-packages.R  
  
# Start Rserve  
ADD start.R start.R  
ADD Rserv.conf /Rserv.conf  
EXPOSE 6311  
CMD Rscript start.R  

