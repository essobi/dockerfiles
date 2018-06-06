  
FROM r-base:latest  
  
# pandoc  
RUN wget
https://github.com/jgm/pandoc/releases/download/2.1.1/pandoc-2.1.1-1-amd64.deb
-O pandoc-2.1.1-1-amd64.deb  
RUN dpkg -i pandoc-2.1.1-1-amd64.deb  
  
# install additional packages  
RUN R -e "install.packages('RColorBrewer', repos = 'http://cran.rstudio.com'
)"  
RUN R -e "install.packages('knitr', repos = 'http://cran.rstudio.com' )"  
RUN R -e "install.packages('markdown', repos = 'http://cran.rstudio.com' )"  
RUN R -e "install.packages('rmarkdown', repos = 'http://cran.rstudio.com' )"  
RUN R -e "install.packages('ggplot2', repos = 'http://cran.rstudio.com' )"  
RUN R -e "install.packages('data.table', repos = 'http://cran.rstudio.com' )"  

