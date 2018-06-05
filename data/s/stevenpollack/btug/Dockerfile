# vim:set ft=dockerfile:  
FROM stevenpollack/docker-rserve  
  
MAINTAINER "Steven Pollack" steven@gnobel.com  
  
# jags for rjags  
# libcurl4 & libssl for devtools  
# libmysqlclient for RMySQL  
RUN apt-get update && \  
apt-get install -y \  
jags \  
libcurl4-openssl-dev \  
libmysqlclient-dev \  
libssl-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
  
# devtools & rjags for BayesianFirstAid  
# hopach for clustering  
# randomForest for classification/regression  
RUN install2.r --error \  
-r "https://cran.rstudio.com" \   
-r "http://www.bioconductor.org/packages/release/bioc" \  
data.table \  
devtools \  
hopach \  
randomForest \  
rjags \  
RMySQL && \  
Rscript -e " \  
options(unzip = 'internal'); \  
httr::set_config( httr::config( ssl_verifypeer = 0L ) ); \  
devtools::install_github('rasmusab/bayesian_first_aid')" && \  
rm -rf /tmp/downloaded_packages/ /tmp/*.rds  
  
# you have to run Rserve with remote=TRUE otherwise  
# it won't let you connect to the container  
EXPOSE 6311  
ENTRYPOINT R -e "\  
library(data.table); \  
library(DBI); \  
library(hopach); \  
library(httr); \  
library(magrittr); \  
library(randomForest); \  
library(RMySQL); \  
library(BayesianFirstAid); \  
# initialize connection to mysql and create \  
# temporary tableau schema  
dbConfig <\- list(); \  
dbConfig[['drv']] <\- MySQL(); \  
dbConfig[['password']] <\- Sys.getenv('MYSQL_ENV_MYSQL_ROOT_PASSWORD'); \  
dbConfig[['port']] <\- as.integer(Sys.getenv('MYSQL_PORT_3306_TCP_PORT')); \  
dbConfig[['host']] <\- Sys.getenv('MYSQL_PORT_3306_TCP_ADDR'); \  
print(str(dbConfig)); \  
tryCatch({ \  
dbConn <\- do.call(dbConnect, dbConfig); \  
dbConn %T>% dbGetQuery('SET NAMES \'utf8\';') %T>% dbGetQuery('CREATE DATABASE
IF NOT EXISTS tableau;') %T>% dbGetQuery('USE tableau;') %>% dbGetQuery('SHOW
DATABASES;');\  
}, error = function(e) { \  
print(e[['message']]); \  
}); \  
Rserve::run.Rserve(remote=TRUE)"  
  

