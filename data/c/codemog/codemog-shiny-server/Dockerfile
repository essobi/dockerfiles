FROM rocker/shiny:latest  
  
MAINTAINER Rob Kemp "robert.kemp@state.co.us"  
RUN apt-get install -y \  
libssl-dev \  
git  
  
RUN R -e "install.packages(c('shiny', 'rmarkdown', 'tm', 'wordcloud',
'memoise', 'dplyr', 'plotly', 'tidyr'), repos='http://cran.rstudio.com/')"  
  
RUN cd /srv/shiny-server && \  
git clone https://github.com/ColoradoDemography/demographic_dashboard  

