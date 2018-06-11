FROM wieling/docker-rstudio-server  
MAINTAINER Martijn Wieling <wieling@gmail.com>  
RUN Rscript -e 'install.packages(c("packrat","httr"),
repos="http://cran.rstudio.com/")'  
ADD .Rprofile /home/guest/.Rprofile  

