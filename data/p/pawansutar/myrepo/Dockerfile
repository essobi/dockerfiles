#FROM r-base  
#COPY . /usr/local/src/myscripts  
#WORKDIR /usr/local/src/myscripts  
#CMD ["Rscript", "simple.R"]  
FROM r-base:latest  
WORKDIR /usr/local/src/myscripts  
COPY . /usr/local/src/myscripts  
RUN apt-get update  
#RUN apt-get install -y libssl-dev libsasl2-dev gcc build-essential g++
zlib1g-dev r-cran-plyr r-cran-reshape2 make autoconf r-cran-ggplot2  
#CMD ["Rscript", "RecommenderMongo_V5.2.R"]  
CMD ["Rscript", "a.R"]  

