# ----------------------------------------  
#  
# This image inherits uoa-inzight-lite-base image,  
# updates packages from docker.stat.auckland.ac.nz  
# repository and installs the shiny app for Lite  
#  
# ----------------------------------------  
FROM scienceis/uoa-inzight-lite-base:dev  
  
MAINTAINER "Science IS Team" ws@sit.auckland.ac.nz  
  
# Edit the following environment variable, commit to Github and it will
trigger Docker build  
# Since we fetch the latest changes from the associated Application~s master
branch  
# this helps trigger date based build  
# The other option would be to tag git builds and refer to the latest tag  
ENV LAST_BUILD_DATE "Sun 13 05 21:45:00 NZDT 2018"  
# Install (via R) all of the necessary packages (R will automatially install
dependencies):  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 381BA480 \  
&& echo "deb http://deb.debian.org/debian stretch main" | sudo tee -a
/etc/apt/sources.list \  
&& apt-get update -y -q \  
  
&& apt-get install -y -q \  
libxml2-dev \  
default-jdk \  
libcurl4-openssl-dev \  
libcairo2-dev \  
libv8-3.14-dev \  
libgdal-dev \  
libproj-dev \  
libprotobuf-dev \  
protobuf-compiler \  
libudunits2-dev \  
libgeos-dev \  
libpq-dev \  
libjq-dev \  
  
&& R -e "update.packages(oldPkgs = 'shiny', repos =
'https://cran.r-project.org', ask = FALSE); install.packages('hextri', repos =
'https://cran.r-project.org', type = 'source'); install.packages('colorspace',
repos = 'https://cran.r-project.org', type = 'source', dependencies = TRUE);
install.packages('RColorBrewer', repos = 'https://cran.r-project.org', type =
'source', dependencies = TRUE); install.packages('viridis', repos =
'https://cran.r-project.org', type = 'source', dependencies = TRUE);
install.packages('XML', repos = 'https://cran.r-project.org', type = 'source',
dependencies = TRUE);
install.packages('https://cran.r-project.org/src/contrib/Archive/gridSVG/gridSVG_1.5-0.tar.gz',
repos = NULL, type = 'source', dependencies = TRUE);
install.packages('RgoogleMaps', repos = 'https://cran.r-project.org',
dependencies = TRUE); install.packages('countrycode', repos =
'https://cran.r-project.org'); update.packages(repos =
'http://r.docker.stat.auckland.ac.nz/R/', ask = FALSE);
install.packages('iNZightMaps', repos =
'http://r.docker.stat.auckland.ac.nz/R/'); install.packages('foreign', repos =
'https://cran.r-project.org', type = 'source', dependencies = TRUE);
install.packages('sas7bdat', repos = 'https://cran.r-project.org', type =
'source', dependencies = TRUE); install.packages('shinyjs', repos =
'https://cran.r-project.org', type = 'source', dependencies = TRUE)" \  
  
&& echo "deb https://cran.stat.auckland.ac.nz/bin/linux/debian jessie-cran34/"
| sudo tee -a /etc/apt/R.list \  
&& apt-get update -y -q \  
&& apt-get upgrade -y -q \  
r-base \  
&& apt-get update -y -q \  
&& apt-get upgrade -y -q \  
  
&& R -e "install.packages('xlsx', repos = 'https://cran.r-project.org', type =
'source', dependencies = TRUE); install.packages('devtools', repos =
'https://cran.r-project.org', type = 'source', dependencies = TRUE);
install.packages('rgeos', repos = 'https://cran.r-project.org', type =
'source', dependencies = TRUE); devtools::install_github('tidyverse/ggplot2');
install.packages('sf', repos = 'https://cran.r-project.org', type = 'source',
dependencies = TRUE)" \  
  
&& apt-get install -y -q \  
gcc-6 \  
g++-6 \  
&& update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-6 60 --slave
/usr/bin/g++ g++ /usr/bin/g++-6 \  
  
&& R -e "install.packages('sf', repos = 'https://cran.r-project.org', type =
'source', dependencies = TRUE); devtools::install_github('daniel-
barnett/ggsfextra'); devtools::install_github('iNZightVIT/iNZightMaps@dev')" \  
  
&& R -e "install.packages('forcats', repos = 'https://cran.r-project.org',
type = 'source', dependencies = TRUE)" \  
&& R -e "install.packages('iNZightTS', repos =
'http://r.docker.stat.auckland.ac.nz/R/')" \  
&& R -e "remove.packages('ggrepel')" \  
&& R -e
"install.packages('https://cran.r-project.org/src/contrib/Archive/ggrepel/ggrepel_0.7.0.tar.gz',
repos = NULL, type = 'source', dependencies = TRUE)" \  
&& R -e "remove.packages('dplyr')" \  
&& R -e
"install.packages('https://cran.r-project.org/src/contrib/Archive/dplyr/dplyr_0.7.4.tar.gz',
repos = NULL, type = 'source', dependencies = TRUE)" \  
  
&& rm -rf /srv/shiny-server/* \  
&& wget --no-verbose -O Lite.zip
https://github.com/iNZightVIT/Lite/archive/master.zip \  
&& unzip Lite.zip \  
&& cp -R Lite-master/* /srv/shiny-server \  
&& echo $LAST_BUILD_DATE > /srv/shiny-server/build.txt \  
&& rm -rf Lite.zip Lite-master/ \  
&& rm -rf /tmp/* /var/tmp/*  
  
# start shiny server process - it listens to port 3838  
CMD ["/opt/shiny-server.sh"]  

