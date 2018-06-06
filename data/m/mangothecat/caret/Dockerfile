FROM rocker/rstudio:3.4.2  
  
RUN apt-get update -qq && apt-get -y --no-install-recommends install \  
libxml2-dev \  
libssl-dev \  
libcurl4-openssl-dev \  
&& . /etc/environment \  
&& install2.r --error \  
\--repos 'http://www.bioconductor.org/packages/release/bioc' \  
\--repos $MRAN \  
tidyverse \  
caret \  
randomForest \  
e1071 \  
gbm \  
RANN \  
glmnet \  
rpart.plot \  
mangoTraining  
  
  
# Add some default app. @TODO Should plumbapp.sh not be an R script?  
ADD auto-mpg.csv /home/rstudio/auto-mpg.csv  
ADD day.csv /home/rstudio/day.csv  
  
# Plumb your app into 8000  
EXPOSE 8787  

