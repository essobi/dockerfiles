# r-lang  
# Ubuntu with R. You can connect with ssh and also run GUI apps (see
bmpvieira/ssh).  
#  
# VERSION 0.0.1  
FROM bmpvieira/ssh  
MAINTAINER Bruno Vieira <mail@bmpvieira.com>  
  
# Add R repository  
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu precise/" >>
/etc/apt/sources.list ;\  
gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9 ;\  
gpg -a --export E084DAB9 | sudo apt-key add -  
  
# Update packages  
RUN apt-get update  
  
# Install R  
RUN apt-get install -y r-recommended  
  
# Set default mirror to avoid requiring user input during automatic installs  
RUN echo 'options(repos=structure(c(CRAN="http://cran.rstudio.com/")))' >
.Rprofile  

