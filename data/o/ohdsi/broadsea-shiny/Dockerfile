FROM rocker/shiny  
  
MAINTAINER Lee Evans - www.ltscomputingllc.com  
  
RUN apt-get update && apt-get install -y default-jdk  
  
RUN R -e " install.packages(c( \  
'rJava', \  
'ggplot2', \  
'shinydashboard', \  
'DT', \  
'pROC', \  
'SqlRender', \  
'EmpiricalCalibration' \  
), repos='http://cran.rstudio.com/') "  

