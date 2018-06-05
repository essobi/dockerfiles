FROM r-base  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends procps && apt-get install -y
libcurl4-gnutls-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget https://cran.r-project.org/src/contrib/chron_2.3-48.tar.gz && R CMD
INSTALL --build chron_2.3-48.tar.gz && rm chron_2.3-48.tar.gz  
  
RUN wget https://cran.r-project.org/src/contrib/data.table_1.10.0.tar.gz && R
CMD INSTALL --build data.table_1.10.0.tar.gz && rm data.table_1.10.0.tar.gz  
  
RUN wget https://cran.r-project.org/src/contrib/Rcpp_0.12.8.tar.gz && R CMD
INSTALL --build Rcpp_0.12.8.tar.gz && rm Rcpp_0.12.8.tar.gz  
RUN wget https://cran.r-project.org/src/contrib/curl_2.3.tar.gz && R CMD
INSTALL --build curl_2.3.tar.gz && rm curl_2.3.tar.gz  
RUN wget https://cran.r-project.org/src/contrib/assertthat_0.1.tar.gz && R CMD
INSTALL --build assertthat_0.1.tar.gz && rm assertthat_0.1.tar.gz  
RUN wget https://cran.r-project.org/src/contrib/lazyeval_0.2.0.tar.gz && R CMD
INSTALL --build lazyeval_0.2.0.tar.gz && rm lazyeval_0.2.0.tar.gz  
RUN wget https://cran.r-project.org/src/contrib/tibble_1.2.tar.gz && R CMD
INSTALL --build tibble_1.2.tar.gz && rm tibble_1.2.tar.gz  
RUN wget https://cran.r-project.org/src/contrib/hms_0.3.tar.gz && R CMD
INSTALL --build hms_0.3.tar.gz && rm hms_0.3.tar.gz  
RUN wget https://cran.r-project.org/src/contrib/R6_2.2.0.tar.gz && R CMD
INSTALL --build R6_2.2.0.tar.gz && rm R6_2.2.0.tar.gz  
RUN wget https://cran.r-project.org/src/contrib/BH_1.62.0-1.tar.gz && R CMD
INSTALL --build BH_1.62.0-1.tar.gz && rm BH_1.62.0-1.tar.gz  
RUN wget https://cran.r-project.org/src/contrib/readr_1.0.0.tar.gz && R CMD
INSTALL --build readr_1.0.0.tar.gz && rm readr_1.0.0.tar.gz  
  
RUN wget https://cran.r-project.org/src/contrib/plotrix_3.6-3.tar.gz && R CMD
INSTALL --build plotrix_3.6-3.tar.gz && rm plotrix_3.6-3.tar.gz  
  
RUN apt-get update && apt-get install -y libcairo2-dev xorg-dev && rm -rf
/var/lib/apt/lists/*  
  
RUN wget https://cran.r-project.org/src/contrib/Cairo_1.5-9.tar.gz && R CMD
INSTALL --build Cairo_1.5-9.tar.gz && rm Cairo_1.5-9.tar.gz  
  
RUN wget http://homepages.uni-regensburg.de/~wit59712/easyqc/EasyQC_9.2.tar.gz
&& R CMD INSTALL --build EasyQC_9.2.tar.gz && rm EasyQC_9.2.tar.gz  
RUN wget https://cran.r-project.org/src/contrib/qqman_0.1.2.tar.gz && R CMD
INSTALL --build qqman_0.1.2.tar.gz && rm qqman_0.1.2.tar.gz  
RUN wget http://csg.sph.umich.edu/abecasis/Metal/download/Linux-metal.tar.gz
&& tar -xf Linux-metal.tar.gz && rm Linux-metal.tar.gz  

