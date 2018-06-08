FROM rocker/shiny:latest  
RUN R -e "install.packages('codetools', repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages('Rcpp', repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages('shiny', repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages('dplyr', repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages('shinyBS', repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages('lattice', repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages('rmarkdown', repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages('Defaults', repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages('tidyr', repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages('quantmod', repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages('PerformanceAnalytics',
repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages('ggvis', repos='http://cran.rstudio.com/')"  
RUN R -e "install.packages('ggplot2', repos='http://cran.rstudio.com/')"  
COPY data-analysis/ /srv/shiny-server/data-analysis  
  

