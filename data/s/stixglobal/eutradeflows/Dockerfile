FROM rocker/shiny  
  
MAINTAINER Paul Rougieux "https://github.com/paulrougieux/"  
# Install dependencies  
# * libmariadb-client-lgpl-dev is required by the RMySQL package  
# * mariadb-client is used as a mysql client and for mysqldump  
RUN apt-get update && apt-get install -y \  
libmariadb-client-lgpl-dev \  
mariadb-client \  
libcurl4-openssl-dev \  
libssl-dev  
  
# Install R Packages  
RUN install2.r --error \  
data.table \  
dbplyr \  
dplyr \  
devtools \  
DT \  
dygraphs \  
ggplot2 \  
lubridate \  
plotly \  
RMySQL \  
shinydashboard \  
stringr \  
tidyr  
  
# Set the working directory to /R  
WORKDIR /R  
  
# Copy the current directory contents into the container at /R/tradeharvester  
ADD . /R/eutradeflows  
  
RUN R CMD build eutradeflows  
  
# R CMD build generates a file name from the description file  
# Remember to update file name here below after a version update  
RUN R -e 'install.packages("eutradeflows_0.0.1.tar.gz")'  
  
# Install dependencies  
# RUN R -e 'devtools::install_github("EuropeanForestInstitute/tradeflows")'  

