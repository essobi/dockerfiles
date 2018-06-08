FROM ruby:2.3.0  
  
# Run updates  
RUN apt-get update -qq && apt-get install -y r-base  
RUN Rscript -e "install.packages('randomForest', dependencies=TRUE,
repos='http://cran.us.r-project.org')"  
RUN Rscript -e "install.packages('TTR', dependencies=TRUE,
repos='http://cran.rstudio.com/')"  

