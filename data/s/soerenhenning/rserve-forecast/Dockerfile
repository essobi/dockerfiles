# Use Ubuntu Xenial Xerus  
FROM ubuntu:xenial  
MAINTAINER SoerenHenning  
  
RUN echo 'deb http://cran.r-project.org/bin/linux/ubuntu xenial/' >>
/etc/apt/sources.list.d/cran.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9  
RUN apt-get update && apt-get install -y r-base  
  
# Log R version  
RUN R --version  
  
# Install R packages  
ADD install-packages.R install-packages.R  
RUN Rscript install-packages.R  
  
# Start Rserve  
ADD start.R start.R  
ADD Rserv.conf /Rserv.conf  
EXPOSE 6311  
CMD Rscript start.R  

