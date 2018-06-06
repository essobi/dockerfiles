FROM rocker/tidyverse  
MAINTAINER Chris Haid <chaid@kippchicago.org>  
  
  
RUN apt-get update -y && apt-get install -y \  
default-jdk \  
libbz2-dev \  
libpcre3-dev \  
liblzma-dev \  
libicu-dev  
  
# add R packages necessary for jobs to run.  
RUN R -e "install.packages('tidyverse', repo = 'cran.rstudio.com')"  
  
RUN R -e "install.packages('bindrcpp', repo = 'cran.rstudio.com')"  
  
RUN R -e "install.packages('plogr', repo = 'cran.rstudio.com')"  
  
RUN R -e "devtools::install_github('hadley/dplyr')"  
  
RUN R -e "install.packages(c('ETLUtils', 'RJDBC'))"  
  
RUN R -e "install.packages('RSQLServer')"  
  
RUN R -e "install.packages('googlesheets')"  
  
RUN R -e "devtools::install_github('almartin82/mapvizieR')"  
  
RUN R -e "devtools::install_github('rstudio/flexdashboard')"  
  
RUN R -e "devtools::install_github('rstudio/DT')"  
  
RUN R -e "install.packages('zoo')"  
  
RUN R -e "devtools::install_github('kippchicago/deanslistr')"  
  
RUN R -e "install.packages('futile.logger')"  
  
RUN R -e "install.packages('googleCloudStorageR')"  
  
RUN R -e "devtools::install_github('kippchicago/silounloadr')"  
  
RUN R -e "install.packages('curl')"  
  
RUN R -e "install.packages('httr')"  
  
RUN R -e "devtools::install_github('kippchicago/teachboostr')"  
  
RUN R -e "install.packages('dplyr')"  
  
RUN R -e "install.packages('dbplyr')"  
  
RUN R -e "install.packages('janitor')"  
  
RUN R -e "install.packages('snakecase')"  
  
RUN R -e " devtools::install_github('rstats-db/bigrquery')"  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
clang \  
libssl-dev  
  
RUN mkdir -p $HOME/.R/ \  
&& echo "\nCXX=clang++ -ftemplate-depth-256\n" >> $HOME/.R/Makevars \  
&& echo "CC=clang\n" >> $HOME/.R/Makevars \  
&& echo "CXXFLAGS=-O3 -mtune=native -march=native -Wno-unused-variable -Wno-
unused-function -Wno-macro-redefined\n" >> $HOME/.R/Makevars  
  
RUN ln -s /usr/lib/x86_64-linux-gnu/libgfortran.so.3 /usr/lib/libgfortran.so  
  
# Install rstan  
RUN install2.r --error \  
inline \  
RcppEigen \  
StanHeaders \  
# rstan \  
KernSmooth  
  
RUN mkdir -p /home/rstudio/.R/ \  
&& echo "\nCXX=clang++ -ftemplate-depth-256\n" >> /home/rstudio/.R/Makevars \  
&& echo "CC=clang\n" >> /home/rstudio/.R/Makevars \  
&& echo "CXXFLAGS=-O3\n" >> /home/rstudio/.R/Makevars \  
&& echo "\nrstan::rstan_options(auto_write = TRUE)" >> /home/rstudio/.Rprofile
\  
&& echo "options(mc.cores = parallel::detectCores())" >>
/home/rstudio/.Rprofile  
  
RUN R -e "install.packages('rstan', repos = 'https://cloud.r-project.org/',
dependencies=TRUE)"  
  
RUN R -e "install.packages('prophet')"  
# add Python for scripts that require python  
# install cron and update tz  
RUN apt-get update &&\  
apt-get install -y --no-install-recommends \  
cron && \  
cp /usr/share/zoneinfo/America/Chicago /etc/localtime && \  
echo "America/Chicago" > /etc/timezone  
  
#RUN install supervisor  
RUN apt-get install -y supervisor  
  
# add jobs  
RUN mkdir /jobs  
#COPY jobs /jobs  
# add crontab  
#COPY crontab /etc/cron.d/idea-cron  
# ADD supervisrd.conf  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# set permissions  
#RUN chmod 0644 /etc/cron.d/idea-cron  
RUN mkdir /data && chmod 777 /data  
  
# Create the log file to be able to run tail  
#RUN touch /var/log/cron.log  
# load crontab  
#RUN crontab /etc/cron.d/idea-cron  
# Run the command on container startup  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  
#CMD /usr/bin/supervisrd/supervisord -c
/etc/supervisor/conf.d/supervisord.conf &&\  
# cron && tail -f /var/log/cron.log && \  
# chown -R rstudio:staff /data  

