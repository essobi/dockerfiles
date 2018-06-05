FROM rocker/r-base  
  
MAINTAINER kirillseva "https://github.com/kirillseva"  
  
ENV GITHUB_PAT 3a3df267be83465757a23f553305a7985526a737  
# Install a bunch of stuff  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update  
  
RUN apt-get install -y --force-yes \  
git \  
curl \  
libcurl3 \  
libcurl4-openssl-dev \  
postgresql-client \  
s3cmd \  
libssl-dev \  
libssl1.0.0 \  
libxml2-dev \  
default-jre \  
default-jdk \  
libv8-dev \  
libpq-dev \  
\--no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
  
# damn lib-pq  
# RUN apt-get install -y --force-yes libpq-dev  
# Install R packages  
RUN install2.r --error \  
bitops \  
devtools \  
httpuv \  
jsonlite \  
RJDBC \  
AUC \  
knitr \  
httr \  
caret \  
zoo \  
gbm \  
rjson \  
pROC \  
XML \  
microbenchmark \  
plyr \  
base64enc \  
yaml \  
digest \  
stringr \  
RJSONIO \  
glmnet \  
RPostgreSQL \  
zoo \  
xts \  
dplyr \  
e1071 \  
R.utils \  
stringi  
  
RUN installGithub.r \  
hadley/purrr \  
hadley/testthat \  
rstats-db/DBI \  
rstats-db/RPostgres \  
avantcredit/aws-tools \  
robertzk/testthatsomemore \  
robertzk/microserver \  
robertzk/objectdiff \  
robertzk/syberiaStructure \  
robertzk/berdie \  
robertzk/stagerunner \  
robertzk/mungebits \  
avantcredit/statsUtils \  
robertzk/syberiaMungebits \  
robertzk/syberiaStages \  
robertzk/Ramd \  
robertzk/director \  
robertzk/rds2 \  
hadley/httr  
  
RUN installGithub.r \  
robertzk/tundra \  
robertzk/director \  
robertzk/productivus \  
robertzk/cachemeifyoucan \  
avantcredit/r-servicetests \  
robertzk/s3mpi \  
robertzk/syberia \  
robertzk/bettertrace \  
robertzk/lockbox \  
peterhurford/batchman \  
kirillseva/dokk \  
kirillseva/ruigi \  
kirillseva/covr \  
peterhurford/batbelt \  
iveksl2/quantmod \  
robertzk/LookR && \  
Rscript -e 'devtools::install_github("FeiYeYe/xgboost", subdir = "R-package")'  
  
CMD ["R"]  

