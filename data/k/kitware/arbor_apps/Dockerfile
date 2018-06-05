FROM rocker/tidyverse  
  
RUN apt-get update && apt-get install -y libgsl-dev  
RUN gsl-config --version  
RUN Rscript -e 'install.packages(c("diversitree"),
repos=c("http://cran.cnr.Berkeley.edu"))'  
RUN R -e
'options(repos="http://cran.cnr.Berkeley.edu");library(devtools);install_github("arborworkflows/aRbor")'  
  
COPY run.R tasks.json anolis.csv anolis.phy ./  
  
ENTRYPOINT ["Rscript", "--vanilla", "--verbose", "run.R"]  

