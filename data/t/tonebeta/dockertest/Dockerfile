FROM quantumobject/docker-shiny  
  
MAINTAINER tonebeta tonebeta@gmail.com  
  
# install R packages  
RUN R -e "install.packages('shinyjs',repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages('highcharter',repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages('dplyr',repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages('readr',repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages('flexdashboard',repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages('ggplot2',repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages('DT',repos='http://cran.rstudio.com/')"  

