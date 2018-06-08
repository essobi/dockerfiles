FROM kuzmenkov/docker-baseimage:latest  
  
  
#Installation of nesesary package/software for this containers...  
RUN echo "deb http://archive.ubuntu.com/ubuntu `cat
/etc/container_environment/DISTRIB_CODENAME`-backports main restricted
universe" >> /etc/apt/sources.list  
RUN (echo "deb http://cran.mtu.edu/bin/linux/ubuntu `cat
/etc/container_environment/DISTRIB_CODENAME`/" >> /etc/apt/sources.list &&
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9)  
  
## Install some useful tools and dependencies for MRO  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /home/docker  
  
# MRO 3.2.2.  
#RUN wget https://www.dropbox.com/s/xrkzdhm1cq0ll1q/microsoft-r-
open-3.3.2.tar.gz?dl=1 -O microsoft-r-open-3.3.2.tar.gz \  
#&& echo "817aca692adffe20e590fc5218cb6992f24f29aa31864465569057534bce42c7
microsoft-r-open-3.3.2.tar.gz" > checksum.txt \  
# Download, valiate, and unpack  
RUN wget https://www.dropbox.com/s/4wyiwm2ohl2dyv7/microsoft-r-
open-3.4.3.tar.gz?dl=1 -O microsoft-r-open-3.4.3.tar.gz \  
&& echo "BF2CD35A11DB604B1FA8F5F0C0ACF0AE05756020D90FB3F6CBB639337EFCEE5B
microsoft-r-open-3.4.3.tar.gz" > checksum.txt \  
&& sha256sum -c --strict checksum.txt \  
&& tar -xf microsoft-r-open-3.4.3.tar.gz \  
&& cd /home/docker/microsoft-r-open \  
&& ./install.sh -a -u \  
&& ls logs && cat logs/*  
  
# Clean up  
WORKDIR /home/docker  
RUN rm microsoft-r-open-3.4.3.tar.gz \  
&& rm checksum.txt \  
&& rm -r microsoft-r-open  
  
# system libraries of general use  
RUN apt-get update && apt-get install -y \  
sudo \  
pandoc \  
pandoc-citeproc \  
libcurl4-gnutls-dev \  
libcairo2-dev \  
libxt-dev \  
libssl-dev \  
libssh2-1-dev \  
libssl1.0.0 \  
libxml2-dev \  
libssl-dev  
  
# system library dependency for the euler app  
RUN apt-get update && apt-get install -y \  
libmpfr-dev \  
gfortran \  
aptitude \  
libgdal-dev \  
libproj-dev \  
g++ \  
gdebi-core\  
libicu-dev \  
libpcre3-dev\  
libbz2-dev \  
liblzma-dev \  
libnlopt-dev \  
build-essential  
  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:ubuntugis/ubuntugis-unstable  
RUN apt-get update  
RUN apt-get install -y libudunits2-dev libgdal-dev libgeos-dev  
  
RUN sudo apt-add-repository -y ppa:webupd8team/java \  
&& apt-get update && echo "oracle-java8-installer shared/accepted-oracle-
license-v1-1 select true" | sudo debconf-set-selections && apt-get install -y
oracle-java8-installer \  
&& R -e "Sys.setenv(JAVA_HOME = '/usr/lib/jvm/java-8-oracle/jre')"  
RUN sudo java -version  
  
COPY Makeconf /usr/lib64/microsoft-r/3.4/lib64/R/etc/Makeconf  
# libproj-de  
#wget https://www.dropbox.com/s/hl0vx1f6rpfgxrx/shiny-
server-1.5.3.838-amd64.deb?dl=1 -O shiny-server-1.5.3.838-amd64.deb  
RUN wget https://www.dropbox.com/s/zjydeqye63dm7ra/shiny-
server-1.5.5.872-amd64.deb?dl=1 -O shiny-server-1.5.5.872-amd64.deb \  
&& dpkg -i --force-depends shiny-server-1.5.5.872-amd64.deb \  
&& rm shiny-server-1.5.5.872-amd64.deb && \  
R -e "install.packages(c('shiny', 'rmarkdown'),
repos='https://cran.rstudio.com/')" \  
&& mkdir -p /srv/shiny-server; sync \  
&& mkdir -p /srv/shiny-server/examples; sync  
# && rm -rf /var/lib/apt/lists/*  
#COPY Makeconf /usr/lib64/microsoft-r/3.3/lib64/R/etc/Makeconf  
RUN mkdir -p /etc/my_init.d  
COPY startup.sh /etc/my_init.d/startup.sh  
RUN chmod +x /etc/my_init.d/startup.sh  
  
##Adding Deamons to containers  
RUN mkdir /etc/service/shiny-server /var/log/shiny-server ; sync  
COPY shiny-server.sh /etc/service/shiny-server/run  
RUN chmod +x /etc/service/shiny-server/run \  
&& cp /var/log/cron/config /var/log/shiny-server/ \  
&& chown -R shiny /var/log/shiny-server \  
&& sed -i '113 a <h2><a href="./examples/">Other examples of Shiny
application</a> </h2>' /srv/shiny-server/index.html  
  
# basic shiny functionality  
RUN R -e "install.packages('binom', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('dplyr', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('ggplot2', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('reshape', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('curl', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('httr', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('devtools', repos='https://cran.r-project.org/')" \  
#&& R -e "install.packages('remotes', repos='https://cran.r-project.org/')" \  
#&& R -e
"remotes::install_url('https://cran.r-project.org/src/contrib/httpuv_1.4.3.tar.gz')"
\  
&& R -e "options(unzip = 'internal'); options(unzip = '/usr/bin/unzip');
devtools::install_github('rstudio/httpuv')" \  
&& R -e "options(unzip = 'internal');
devtools::install_github('rstudio/shiny')" \  
&& R -e "install.packages('formattable', repos='https://cran.r-project.org/')"
\  
&& R -e "install.packages('car', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('fmsb', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('igraph', repos='https://cran.r-project.org/')" \  
&& sudo su - -c "R -e \"install.packages('miniUI',
repos='https://cran.r-project.org/');options(unzip = 'internal');
devtools::install_github('daattali/shinyjs')\"" \  
#RUN R -e "options(unzip = 'internal');
devtools::install_github('daattali/shinyjs')" \  
&& R -e "install.packages('scales', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('crosstalk', repos='https://cran.r-project.org/')" \  
&& sudo su - -c "R -e \"options(unzip = 'internal');
devtools::install_github('rstudio/DT')\"" \  
#RUN R -e "devtools::install_github('rstudio/DT')" \  
&& sudo su - -c "R -e \"install.packages(c('raster', 'sp', 'viridis'),
repos='https://cran.r-project.org/');options(unzip = 'internal');
devtools::install_github('rstudio/leaflet')\"" \  
&& sudo su - -c "R -e \"options(unzip = 'internal');
devtools::install_github('bhaskarvk/leaflet.extras')\"" \  
&& R -e "install.packages('ggrepel', repos='https://cran.r-project.org/')" \  
#RUN R -e "install.packages('leaflet', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('visNetwork', repos='https://cran.r-project.org/')"
\  
&& R -e "install.packages('purrr', repos='https://cran.r-project.org/')" \  
&& sudo su - -c "R -e \"options(unzip = 'internal');
devtools::install_github('kuzmenkov111/highcharter')\"" \  
#&& sudo su - -c "R -e \"options(unzip = 'internal');
devtools::install_version('highcharter', version = '0.5.0', repos =
'https://cran.r-project.org/')\"" \  
#RUN R -e "download.file(url =
'http://cran.r-project.org/src/contrib/Archive/highcharter/highcharter_0.3.0.tar.gz',
destfile = 'highcharter_0.3.0.tar.gz')"  
#RUN R -e "install.packages(pkgs='highcharter_0.3.0.tar.gz', type='source',
repos=NULL)"  
#RUN R -e "unlink('highcharter_0.3.0.tar.gz')"  
&& R -e "install.packages('shinyBS', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('data.table', repos='https://cran.r-project.org/')"
\  
&& R -e "install.packages('maptools', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('rgdal', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('googleVis', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('future', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('tidyr', repos='https://cran.r-project.org/')"\  
&& sudo su - -c "R -e \"options(unzip = 'internal');
devtools::install_github('daattali/timevis')\""\  
&& R -e "install.packages('shinythemes', repos='https://cran.r-project.org/')"
\  
&& R -e "install.packages('formattable', repos='https://cran.r-project.org/')"
\  
&& R -e "install.packages('fst', repos='https://cran.r-project.org/')" \  
#&& sudo su - -c "R -e \"options(unzip = 'internal');
devtools::install_version('fst', version = '0.7.2', repos =
'https://cran.r-project.org/')\"" \  
&& R -e "install.packages('leaflet.minicharts',
repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('RColorBrewer',
repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('grDevices', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('gplots', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('shinyWidgets',
repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('shinyjqui', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('collapsibleTree',
repos='https://cran.r-project.org/')" \  
#&& sudo su - -c "R -e \"options(unzip = 'internal');
devtools::install_github('kuzmenkov111/shinyURL')\"" \  
&& R -e "install.packages('RCurl', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('shinycssloaders',
repos='https://cran.r-project.org/')" \  
#&& sudo R -e "install.packages('ReporteRs',
repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('officer', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('flextable', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('raster', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('digest', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('bcrypt', repos='https://cran.r-project.org/')" \  
&& sudo su - -c "R -e \"options(unzip = 'internal');
devtools::install_github('hrbrmstr/qrencoder')\"" \  
&& R -e "install.packages('rgdal', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('mapview', repos='https://cran.r-project.org/')" \  
&& R CMD javareconf \  
&& R -e "Sys.setenv(JAVA_HOME = '/usr/lib/jvm/java-8-oracle/jre');
install.packages('rJava', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('mailR', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('RPostgres', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('stringi', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('pool', repos='https://cran.r-project.org/')" \  
&& R -e "install.packages('DBI', repos='https://cran.r-project.org/')"  
  
COPY shiny-server.conf /etc/shiny-server/shiny-server.conf  
RUN mkdir /var/lib/shiny-server/bookmarks \  
&& chown -R shiny:shiny /var/lib/shiny-server/bookmarks  
  
RUN sudo rm -rf /srv/shiny-server/sample-apps \  
&& rm -rf /srv/shiny-server/  
  
#volume for Shiny Apps and static assets. Here is the folder for
index.html(link) and sample apps.  
VOLUME /srv/shiny-server  
EXPOSE 3838  
CMD ["/sbin/my_init"]  

