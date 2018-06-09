# Docker file for TED-tags  
# Charley Carriero, 12-Dec-2017  
# use rocker/tidyverse as the base image and  
FROM rocker/tidyverse  
  
# then install the ezknitr, lubridate, readr and stringr  
RUN Rscript -e "install.packages('ezknitr', repos =
'https://mran.revolutionanalytics.com/snapshot/2017-12-11')"  
  
RUN Rscript -e "install.packages('lubridate', repos =
'https://mran.revolutionanalytics.com/snapshot/2017-12-11')"  
  
RUN Rscript -e "install.packages('readr', repos =
'https://mran.revolutionanalytics.com/snapshot/2017-12-11')"  
  
RUN Rscript -e "install.packages('stringr', repos =
'https://mran.revolutionanalytics.com/snapshot/2017-12-11')"  
  
RUN Rscript -e "install.packages('packrat', repos =
'https://mran.revolutionanalytics.com/snapshot/2017-12-11')"

