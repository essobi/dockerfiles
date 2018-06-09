FROM zapster/latex  
MAINTAINER Josef Eisl <zapster@zapster.cc>  
  
USER root  
RUN dnf -y update && dnf clean all  
RUN dnf -y install \  
R \  
&& dnf clean all  
  
USER docker  
  
ENV R_LIBS="/home/docker/R_libs"  
RUN mkdir -p $R_LIBS  
RUN Rscript -e
'install.packages(c("ggplot2","reshape2","dplyr","RColorBrewer"),
repos="http://cran.rstudio.com/", clean=TRUE)'  
  
CMD ["bash"]  

