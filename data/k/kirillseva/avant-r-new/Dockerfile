FROM kirillseva/avant-r  
  
MAINTAINER kirillseva "https://github.com/kirillseva"  
  
ENV GITHUB_PAT 382ef2b9b3bcf4127047c4e146148c6179fe66c0  
  
RUN apt-get update \  
&& apt-get install -y libssl-dev/unstable \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN installGithub.r \  
jimhester/withr \  
hadley/memoise \  
hadley/devtools \  
rcppcore/rcpp && \  
Rscript -e 'install.packages("RCurl")' && \  
Rscript -e 'install.packages("rJava")' && \  
Rscript -e 'install.packages("rredis")'  
  
RUN installGithub.r \  
hadley/plyr \  
jeroenooms/openssl \  
jeroenooms/curl \  
Rexamine/stringi \  
robertzk/Ramd \  
hadley/stringr \  
RCppCore/RCpp \  
rstats-db/DBI \  
robertzk/RPostgres@fix_type_issues \  
gaborcsardi/praise \  
robertzk/recombinator \  
syberia/dbtest \  
cran/stringi \  
jeroenooms/jsonlite \  
cran/rversions \  
robertzk/hipchat \  
kirillseva/slackr \  
robertzk/cachemeifyoucan \  
robertzk/stagerunner \  
robertzk/director \  
robertzk/rds2 \  
robertzk/testthatsomemore \  
robertzk/berdie \  
robertzk/mungebits \  
robertzk/microserver \  
hadley/testthat@v0.10.0 \  
hadley/httr \  
RCppCore/Rcpp \  
cran/base64enc \  
kirillseva/covr \  
wch/R6@v2.1.1  
  
RUN installGithub.r \  
kirillseva/cacher \  
robertzk/productivus \  
robertzk/cachemeifyoucan \  
robertzk/s3mpi \  
syberia/syberia@0.4-stable \  
gaborcsardi/crayon \  
cran/arules \  
cran/TTR \  
edwindj/whisker \  
avantcredit/statsutils \  
robertzk/bettertrace \  
robertzk/lockbox \  
peterhurford/batchman \  
kirillseva/rain \  
kirillseva/ruigi \  
avantcredit/make_validation_plot \  
avantcredit/FookR \  
robertzk/LookR && \  
Rscript -e 'install.packages("quantmod")' \  
Rscript -e 'install.packages("crayon")'  
  
RUN R CMD javareconf  
  
CMD ["R"]  

