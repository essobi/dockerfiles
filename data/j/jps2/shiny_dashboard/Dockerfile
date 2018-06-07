FROM rocker/shiny  
  
RUN apt-get update \  
&& apt-get install -y -f libv8-dev libxml2-dev libssl-dev  
  
## Configure default locale, see https://github.com/rocker-
org/rocker/issues/19  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen en_US.utf8 \  
&& /usr/sbin/update-locale LANG=en_US.UTF-8  
  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
RUN R -e "install.packages(c('httr', 'dplyr', 'tidyr','jsonlite'),
repos='https://cran.rstudio.com/')"  
  
RUN R -e "install.packages(c('V8','shinyjs', 'shinydashboard',
'RColorBrewer','plotly'), repos='https://cran.rstudio.com/')"  
RUN R -e "install.packages(c('lubridate', 'reshape2'),
repos='https://cran.rstudio.com/')"  
  
# cran package is 1.5.7, we need latest version  
RUN R -e "install.packages(c('devtools'), repos='https://cran.rstudio.com/')"  
RUN R -e "devtools::install_github(c('ramnathv/htmlwidgets',
'smartinsightsfromdata/rpivotTable'))"  
RUN R -e "install.packages(c('shinyBS'), repos='https://cran.rstudio.com/')"  
RUN R -e "install.packages(c('ggplot2','cowplot','grid'),
repos='https://cran.rstudio.com/')"  

