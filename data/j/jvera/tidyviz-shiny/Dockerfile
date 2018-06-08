FROM rocker/shiny:latest  
  
LABEL maintainer "vera.josemanuel [AT] gmail dot com"  
  
RUN R -e "install.packages('ggplot2', repos='https://cran.rstudio.com/')"  
  
EXPOSE 3838  
COPY shiny-server.sh /usr/bin/shiny-server.sh  
  
CMD ["/usr/bin/shiny-server.sh"]  

