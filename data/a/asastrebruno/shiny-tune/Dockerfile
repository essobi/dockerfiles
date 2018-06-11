FROM rocker/shiny  
  
RUN Rscript -e
'install.packages(c("data.table","ggplot2","shinydashboard","DT","jsonlite"),repos="https://cloud.r-project.org/")'  
  
RUN apt-get update; apt-get install -y libssl-dev  
  
RUN Rscript -e
'install.packages(c("plotly"),repos="https://cloud.r-project.org/")'  
  
USER shiny

