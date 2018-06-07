FROM rocker/rstudio  
  
MAINTAINER Chia-Chi Chang <c3h3.tw@gmail.com>  
  
RUN GIT_SSL_NO_VERIFY=true git clone
https://github.com/johnmyleswhite/ML_for_Hackers.git /demo/ML_for_iHackers  
RUN cd /demo/ML_for_iHackers && Rscript package_installer.R  
  
ADD userconf.sh /usr/bin/userconf.sh  
RUN chmod a+x /usr/bin/userconf.sh  
  
ENV DEMOPATH /demo  
  
  

