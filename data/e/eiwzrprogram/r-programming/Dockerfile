FROM r-base:latest  
WORKDIR /usr/local/src/myscripts  
COPY . /usr/local/src/myscripts  
COPY api_push_call.R /usr/local/src/myscripts  
COPY api_push_recom.R /usr/local/src/myscripts  
RUN apt-get update  
RUN apt-get install -y libssl-dev/unstable libsasl2-dev  
RUN apt-get update  
RUN apt-get install -y gcc build-essential g++ zlib1g-dev make autoconf
#r-cran-ggplot2 r-cran-plyr r-cran-reshape2  
RUN apt-get update  
RUN apt-get install -y libcurl4-gnutls-dev libxml2-dev  
#RUN apt-get install -y r-cran-mongolite r-cran-jsonlite r-cran-httr #"^r-.*"  
#CMD ["Rscript", "Recommender_Combin_V2.R"]  
#CMD ["Rscript", "API_Pull.R"]  
CMD ["Rscript", "api_push_call.R"]  

