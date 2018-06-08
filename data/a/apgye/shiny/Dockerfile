FROM r-base:latest  
  
MAINTAINER Winston Chang "winston@rstudio.com"  
# Install dependencies and Download and install shiny server  
RUN apt-get update && apt-get install -y -t unstable \  
sudo \  
gdebi-core \  
pandoc \  
pandoc-citeproc \  
libcurl4-gnutls-dev \  
libcairo2-dev/unstable \  
libxt-dev \  
libnss-wrapper gettext && \  
wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \  
VERSION=$(cat version.txt) && \  
wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-
build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb &&
\  
gdebi -n ss-latest.deb && \  
rm -f version.txt ss-latest.deb && \  
R -e "install.packages(c('shiny', 'rmarkdown'),
repos='https://cran.rstudio.com/')" && \  
cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/ && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 3838  
RUN mkdir -p /var/log/shiny-server && chgrp -R 0 /var/log/shiny-server &&
chmod -R g=u /var/log/shiny-server  
  
COPY shiny-server.sh /usr/bin/shiny-server.sh  
COPY shiny-server.conf /etc/shiny-server/shiny-server.conf  
  
ENV USER_NAME=shiny NSS_WRAPPER_PASSWD=/tmp/passwd
NSS_WRAPPER_GROUP=/tmp/group  
RUN touch ${NSS_WRAPPER_PASSWD} ${NSS_WRAPPER_GROUP} && \  
chgrp 0 ${NSS_WRAPPER_PASSWD} ${NSS_WRAPPER_GROUP} &&\  
chmod g+rw ${NSS_WRAPPER_PASSWD} ${NSS_WRAPPER_GROUP}  
ADD passwd.template /passwd.template  
ADD nss_wrapper.sh /nss_wrapper.sh  
  
ENTRYPOINT ["/nss_wrapper.sh"]  
CMD ["shiny-server.sh"]  

