# vast-tools  
# Usage: vast-tools [SUBCOMMAND]  
FROM r-base:3.5.0  
MAINTAINER Nuno Agostinho <nunodanielagostinho@gmail.com>  
  
RUN apt-get update  
  
RUN apt-get install -y bowtie  
RUN apt-get install -y libcurl4-openssl-dev  
RUN apt-get install -y libssl-dev  
RUN apt-get install -y libssh2-1-dev  
RUN apt-get install -y perl  
  
RUN echo "r <\- getOption('repos'); r['CRAN'] <\-
'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile  
RUN Rscript -e "install.packages('optparse')"  
RUN Rscript -e "install.packages('RColorBrewer')"  
RUN Rscript -e "install.packages('reshape2')"  
RUN Rscript -e "install.packages('ggplot2')"  
RUN Rscript -e "install.packages('MASS')"  
RUN Rscript -e "install.packages('devtools')"  
RUN Rscript -e "devtools::install_github('kcha/psiplot')"  
  
ENV SW=/root/software/  
RUN mkdir -p ${SW}  
WORKDIR ${SW}  
ENV vasttools=vast-tools  
COPY ${vasttools} ${vasttools}  
  
ENV PATH="${PATH}:${SW}/${vasttools}"  
RUN locale-gen --purge en_US.UTF-8  
RUN echo -e 'LANG="en_US.UTF-8"\nLANGUAGE="en_US:en"\n' > /etc/default/locale

