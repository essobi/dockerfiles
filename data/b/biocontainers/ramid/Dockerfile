# PhenoMeNal H2020  
FROM ubuntu:16.04  
MAINTAINER PhenoMeNal-H2020 Project ( phenomenal-h2020-users@googlegroups.com
)  
  
LABEL version=0.1  
LABEL software.version=1.0  
LABEL software=ramid  
  
ENV RAMID_REVISION "954bfb3430bb92c96e69e3cbf66b82375848fa02"  
# Setup package repos  
RUN echo "deb http://cloud.r-project.org/bin/linux/ubuntu xenial/" >>
/etc/apt/sources.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9  
  
RUN apt-get -y update && apt-get -y --no-install-recommends install r-base
r-base-dev libssl-dev \  
libcurl4-openssl-dev git \  
libssh2-1-dev r-cran-ncdf4 && \  
echo 'options("repos"="http://cran.rstudio.com")' >> /etc/R/Rprofile.site && \  
R -e "install.packages(c('devtools', 'optparse'))" && \  
R -e 'library(devtools);
install_github("seliv55/RaMID",ref=Sys.getenv("RAMID_REVISION")[1])' && \  
apt-get purge -y git r-base-dev libssl-dev libcurl4-openssl-dev libssh2-1-dev
&& \  
apt-get clean && apt-get autoremove -y && rm -rf
/var/lib/{apt,dpkg,cache,log}/ /tmp/* /var/tmp/*  
  
# Add scripts folder to container  
ADD scripts/runRamid.R /usr/bin/runRamid.R  
  
RUN chmod +x /usr/bin/runRamid.R  
# Define Entry point script  
ENTRYPOINT ["runRamid.R"]  

