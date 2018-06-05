FROM rocker/rstudio  
  
RUN apt-get update \  
&& apt-get install -y texlive-latex-extra \  
&& echo 'install.packages(c("ggplot2", "plyr", "reshape2", "RColorBrewer",
"scales","grid", "wesanderson",
"bigrquery","googleCloudStorageR","rmarkdown","flexdashboard"),
repos="http://cran.us.r-project.org", dependencies=TRUE)' > /tmp/packages.R \  
&& Rscript /tmp/packages.R  
  
EXPOSE 8787  
  
CMD ["/init"]  

