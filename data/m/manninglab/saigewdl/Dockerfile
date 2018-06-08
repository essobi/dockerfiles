FROM r-base:3.4.4  
MAINTAINER TM (tmajaria@broadinstitute.org)  
  
RUN apt-get update && apt-get -y install git dstat libcurl4-openssl-dev
libssl-dev libboost-iostreams-dev  
  
RUN git clone https://github.com/manning-lab/saigeWdl.git && cd ./saigeWdl &&
git pull origin master  
  
RUN echo "r <\- getOption('repos'); r['CRAN'] <\-
'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile  
RUN Rscript -e "install.packages(c('devtools', 'Rcpp', 'RcppArmadillo',
'RcppParallel', 'data.table', 'SPAtest', 'RcppEigen', 'Matrix', 'stringr'))"  
  
RUN wget
https://github.com/weizhouUMICH/SAIGE/raw/master/SAIGE_0.26_R_x86_64-pc-linux-
gnu.tar.gz  
  
RUN R CMD INSTALL SAIGE_0.26_R_x86_64-pc-linux-gnu.tar.gz  
RUN rm -rf SAIGE_0.26_R_x86_64-pc-linux-gnu.tar.gz

