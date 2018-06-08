FROM rocker/tidyverse:latest  
  
# basics  
RUN echo 'install.packages(c("RPostgreSQL", "googlesheets", "futile.logger"),
repos="http://cran.us.r-project.org", dependencies=TRUE)' > /tmp/packages1.R \  
&& Rscript /tmp/packages1.R  
  
# tests  
RUN echo 'install.packages(c("validate", "testthat"),
repos="http://cran.us.r-project.org", dependencies=TRUE)' > /tmp/packages2.R \  
&& Rscript /tmp/packages2.R  
  
# misc  
RUN echo 'install.packages(c("needs", "aws.s3", "data.table", "gmailr"),
repos="http://cran.us.r-project.org", dependencies=TRUE)' > /tmp/packages3.R \  
&& Rscript /tmp/packages3.R  
  
# stats  
RUN echo 'install.packages(c("zoo", "tseries", "forecast", "lme4", "xgboost",
"mgcv", "ranger"), repos="http://cran.us.r-project.org", dependencies=TRUE)' >
/tmp/packages4.R \  
&& Rscript /tmp/packages4.R  
  
# advanced stats  
RUN echo 'install.packages(c("Matrix", "glmnet"),
repos="http://cran.us.r-project.org", dependencies=TRUE)' > /tmp/packages5.R \  
&& Rscript /tmp/packages5.R  
  
# geo  
RUN echo 'install.packages(c("sf", "leaflet"),
repos="http://cran.us.r-project.org", dependencies=TRUE)' > /tmp/packages6.R \  
&& Rscript /tmp/packages6.R  
  
# parallelization  
RUN echo 'devtools::install_github("hadley/multidplyr")' > /tmp/packages7.R \  
&& Rscript /tmp/packages7.R  

