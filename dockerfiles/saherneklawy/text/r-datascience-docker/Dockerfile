FROM r-base:latest

RUN apt-get update && apt-get install -y \
  libmysqlclient-dev

RUN R -e 'install.packages("rmarkdown")'
RUN R -e 'install.packages("shiny")'
RUN R -e 'install.packages("tidyr")'
RUN R -e 'install.packages("dplyr")'
RUN R -e 'install.packages("ggplot2")'
RUN R -e 'install.packages("ggvis")'
RUN R -e 'install.packages("RMySQL")'
RUN R -e 'install.packages("BH")'
RUN R -e 'install.packages("DBI")'
RUN R -e 'install.packages("R6")'
RUN R -e 'install.packages("RColorBrewer")'
RUN R -e 'install.packages("RJSONIO")'
RUN R -e 'install.packages("Rcpp")'
RUN R -e 'install.packages("assertthat")'
RUN R -e 'install.packages("bitops")'
RUN R -e 'install.packages("caTools")'
RUN R -e 'install.packages("colorspace")'
RUN R -e 'install.packages("dichromat")'
RUN R -e 'install.packages("digest")'
RUN R -e 'install.packages("evaluate")'
RUN R -e 'install.packages("formatR")'
RUN R -e 'install.packages("gtable")'
RUN R -e 'install.packages("highr")'
RUN R -e 'install.packages("htmltools")'
RUN R -e 'install.packages("httpuv")'
RUN R -e 'install.packages("jsonlite")'
RUN R -e 'install.packages("knitr")'
RUN R -e 'install.packages("labeling")'
RUN R -e 'install.packages("lazyeval")'
RUN R -e 'install.packages("lubridate")'
RUN R -e 'install.packages("magrittr")'
RUN R -e 'install.packages("markdown")'
RUN R -e 'install.packages("mime")'
RUN R -e 'install.packages("munsell")'
RUN R -e 'install.packages("plyr")'
RUN R -e 'install.packages("proto")'
RUN R -e 'install.packages("reshape2")'
RUN R -e 'install.packages("scales")'
RUN R -e 'install.packages("xtable")'
RUN R -e 'install.packages("yaml")'
RUN R -e 'install.packages("caret")'
RUN R -e 'install.packages("e1071")'
RUN R -e 'install.packages("xgboost")'
RUN R -e 'install.packages("pROC")'

RUN apt-get install -y \
  pandoc

RUN apt-get install -y \
  curl libcurl4-openssl-dev

# readr needs to be installed after curl and libcurl
RUN R -e 'install.packages("readr")'

#RUN apt-get install -y \
#  mongodb-clients \
#  pandoc
