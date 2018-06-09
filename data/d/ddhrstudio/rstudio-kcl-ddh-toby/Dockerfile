FROM rocker/tidyverse  
  
RUN apt-get clean && apt-get -q -y update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -q -y --fix-missing install \  
libbz2-dev \  
libgdal-dev \  
libgeos-dev \  
libgsl-dev \  
libjpeg62-turbo-dev \  
libjq-dev \  
liblzma-dev \  
libprotobuf-dev \  
libudunits2-dev \  
libv8-3.14-dev \  
openjdk-8-jdk \  
protobuf-compiler  
  
RUN install2.r --error \  
GISTools \  
OpenStreetMap \  
NeuralNetTools \  
NeuralNetTools \  
RColorBrewer \  
RedditExtractoR \  
Rfacebook \  
XML \  
arules \  
catdata \  
cluster \  
corrplot \  
devtools \  
dplyr \  
fitdistrplus \  
gapminder \  
ggmap \  
ggplot2 \  
ggraph \  
ggrepel \  
ggvis \  
googleVis \  
graphTweets \  
gsheet \  
gtrendsR \  
gutenbergr \  
httr \  
imputeTS \  
igraph \  
jpeg \  
jsonlite \  
lubridate \  
magrittr \  
maps \  
nnet \  
pageviews \  
plotly \  
quanteda \  
raster \  
recommenderlab \  
reshape2 \  
rpart \  
rtweet \  
rworldmap \  
shiny \  
spatstat \  
swirl \  
tm \  
tmap \  
topicmodels \  
twitteR \  
wikipediatrend \  
wordcloud \  
xts  
  
RUN wget
https://cran.r-project.org/src/contrib/Archive/ngramr/ngramr_1.4.5.tar.gz  
RUN R CMD INSTALL ngramr_1.4.5.tar.gz  
  
#RUN wget
http://cran.r-project.org/src/contrib/Archive/slam/slam_0.1-37.tar.gz  
#RUN R CMD INSTALL slam_0.1-37.tar.gz  
RUN Rscript -e 'install.packages("h2o", type="source",
repos=(c("http://h2o-release.s3.amazonaws.com/h2o/latest_stable_R")))'  
RUN Rscript -e "require(devtools)" -e 'install_github("jbryer/likert")'  
RUN Rscript -e 'require(devtools)' -e 'install_github("robjhyndman/forecast")'  
RUN Rscript -e 'require(devtools)' -e 'install_github("ironholds/pageviews")'  
RUN Rscript -e 'require(devtools)' -e
'install_github("twitter/AnomalyDetection")'  
RUN Rscript -e 'require(devtools)' -e 'install_github("dgrtwo/gganimate")'  
RUN Rscript -e 'require(devtools)' -e 'install_github("PMassicotte/gtrendsR")'  
RUN Rscript -e 'require(devtools)' -e
'install_github("trinker/qdapDictionaries")'  
RUN Rscript -e 'require(devtools)' -e 'install_github("trinker/qdapRegex")'  
RUN Rscript -e 'require(devtools)' -e 'install_github("trinker/qdapTools")'  
RUN Rscript -e 'require(devtools)' -e 'install_github("trinker/qdap")'  
RUN Rscript -e 'source("https://bioconductor.org/biocLite.R")' -e
'biocLite("Rgraphviz")'  
  
RUN Rscript -e 'require(devtools)' -e 'install_github("goto4711/scaddh")'  
  
# Uncomment for online build  
RUN mkdir /courses  
RUN mkdir /swirldata  
  
RUN echo 'session-timeout-minutes=10' > /etc/rstudio/rsession.conf  
  
ADD scripts /  
  

