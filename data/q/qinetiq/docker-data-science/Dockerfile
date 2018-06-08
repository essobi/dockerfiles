  
FROM qinetiq/ubuntu-base-data-science:latest  
  
MAINTAINER Josh Cole <jwcole1@qinetiq.com>  
  
USER root  
  
ADD https://s3.amazonaws.com/rstudio-server/current.ver /tmp/rstudio.ver  
  
RUN apt-get -y update && apt-get -y install libapparmor1 libcurl4-openssl-dev
libxml2-dev libssl-dev gdebi-core apt-transport-https  
  
ENV CRAN_URL https://cloud.r-project.org/  
  
RUN set -e \  
&& R -e "update.packages(ask = FALSE, repos = '${CRAN_URL}'); \  
install.packages(pkgs = c('dbplyr', 'devtools', 'ggmcmc', 'glmnet', 'rstan',
'tidyverse', 'xgboost'), \  
dependencies = TRUE, repos = '${CRAN_URL}');"  
  
RUN set -e \  
&& curl -sS http://download2.rstudio.org/rstudio-server-$(cat
/tmp/rstudio.ver)-amd64.deb -o /tmp/rstudio.deb \  
&& gdebi --non-interactive --option=APT::Get::Assume-Yes="true" -n
/tmp/rstudio.deb  
  
# ~~~~ CLEAN UP ~~~~  
RUN apt-get update && apt-get --yes upgrade && apt-get --yes autoremove &&
apt-get clean && \  
rm -rf /var/lib/apt-get/lists/* && \  
rm -rf /src/*.deb && \  
rm -rf $CONDA_SRC/* && \  
rm -rf /tmp/*  
  
CMD ["/usr/lib/rstudio-server/bin/rserver", "--server-daemonize=0", "--server-
app-armor-enabled=0"]  

