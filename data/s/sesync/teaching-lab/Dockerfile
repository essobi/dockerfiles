FROM debian:stretch-slim  
MAINTAINER "Ian Carroll" icarroll@sesync.org  
  
## FIXME update-alternatives to blame  
## https://github.com/debuerreotype/debuerreotype/issues/10  
RUN mkdir -p \  
/usr/share/man/man1/ \  
/usr/share/man/man7/  
  
# System/Debian Packages  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG C.UTF-8  
  
RUN apt-get update \  
&& apt-get install -yq --no-install-recommends \  
build-essential \  
apt-utils \  
&& apt-get install -yq --no-install-recommends \  
curl \  
gnupg2 \  
nginx \  
openssh-client \  
ca-certificates \  
ruby-dev \  
cron \  
# pgStudio dependency:  
default-jdk \  
&& gem install \  
bundler \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get update \  
&& apt-get install -yq --no-install-recommends \  
# JupyterHub dependency:  
nodejs  
  
  
# Process Supervisor: s6-overlay  
  
RUN curl -sL https://github.com/just-
containers/s6-overlay/releases/download/v1.11.0.1/s6-overlay-amd64.tar.gz |
tar xz  
  
  
# Open Science Libraries/Utilities  
  
RUN apt-get install -yq --no-install-recommends \  
libgdal-dev \  
python-gdal \  
libudunits2-dev \  
libnlopt-dev \  
libgsl-dev \  
git \  
libcairo2-dev \  
libmagick++-dev \  
libspatialindex-c4v5 \  
&& git config --global push.default upstream  
  
  
# R and RStudio  
  
ADD root/etc/apt/sources.list.d/debian-cran.list
/etc/apt/sources.list.d/debian-cran.list  
ADD cran.gpg.key .  
RUN gpg --import cran.gpg.key \  
&& gpg --export --armor E19F5F87128899B192B1A2C2AD5F960A256A04AF | apt-key add
- \  
&& rm cran.gpg.key \  
&& apt-get update \  
&& apt-get install -yq --no-install-recommends \  
libcurl4-openssl-dev \  
libxml2-dev \  
libssl-dev \  
&& apt-get install -yq --no-install-recommends \  
r-base \  
r-base-dev \  
libapparmor1 \  
gdebi-core  
### FIXME outdated library is hardcoded in rstudio server  
### https://support.rstudio.com/hc/en-
us/community/posts/115005872767-R-Studio-Server-install-fails-hard-coded-
libssl1-0-0-dependency-out-of-date-  
RUN curl -sL
http://ftp.debian.org/debian/pool/main/o/openssl/libssl1.0.0_1.0.1t-1+deb8u7_amd64.deb
-o libssl1.0.0.deb \  
&& dpkg -i libssl1.0.0.deb \  
&& rm libssl1.0.0.deb  
RUN curl -sL https://download2.rstudio.org/rstudio-server-1.1.442-amd64.deb -o
rstudio.deb \  
&& gdebi --non-interactive rstudio.deb \  
&& rm rstudio.deb  
  
  
# Python and JupyterLab  
  
RUN apt-get install -yq --no-install-recommends \  
python3 \  
python3-dev \  
python3-pip \  
&& python3 -m pip install --upgrade pip \  
&& python3 -m pip install \  
setuptools \  
wheel \  
&& python3 -m pip install \  
tornado \  
jinja2 \  
traitlets \  
jupyter \  
jupyterlab \  
jupyterhub \  
jupyter-console \  
ipywidgets \  
bash_kernel \  
&& jupyter serverextension enable --py jupyterlab --sys-prefix \  
&& jupyter labextension install @jupyterlab/hub-extension \  
&& jupyter labextension install @jupyterlab/geojson-extension \  
&& python3 -m bash_kernel.install \  
&& npm install -g \  
configurable-http-proxy  
  
### FIXME prevent JupyterHub's username -> lowercase "normalization"  
RUN sed -e "/username = username.lower()/d" -i /usr/local/lib/python3.5/dist-
packages/jupyterhub/auth.py  
  
  
# PostgreSQL  
  
RUN apt-get install -yq --no-install-recommends \  
postgresql \  
postgresql-contrib \  
postgis \  
&& usermod -a -G shadow postgres  
  
## pgStudio (java requiremnt; software is in /usr/share/pgstudio)  
  
RUN apt-get install -yq --no-install-recommends \  
default-jdk  
  
# QGIS  
  
ADD root/etc/apt/sources.list.d/debian-qgis.list
/etc/apt/sources.list.d/debian-qgis.list  
ADD qgis.gpg.key .  
RUN gpg --import qgis.gpg.key \  
&& gpg --export --armor CAEB3DC3BDF7FB45 | apt-key add - \  
&& rm qgis.gpg.key \  
&& apt-get update \  
&& apt-get install -yq --no-install-recommends \  
qgis \  
python-qgis  
  
  
# Packages for Building and Serving Lessons  
  
RUN apt-get install -yq --no-install-recommends \  
ruby \  
emacs \  
rsync \  
&& python3 -m pip install \  
pweave \  
pyyaml  
# rise \  
# && jupyter-nbextension install rise --py --sys-prefix \  
# && jupyter-nbextension enable rise --py --sys-prefix  
  
  
# Packages for Lessons  
  
## Python Packages  
  
RUN python3 -m pip install \  
beautifulsoup4 \  
census \  
geopandas \  
ggplot \  
lxml \  
matplotlib \  
numpy \  
pandas \  
pygresql \  
pydap \  
rasterio \  
requests \  
sqlalchemy  
  
## R Packages  
  
RUN echo "options(repos = c(CRAN = 'https://cran.rstudio.com/'),
download.file.method = 'libcurl')" >> /usr/lib/R/etc/Rprofile.site \  
&& Rscript -e "install.packages(c( \  
'base64enc', \  
'bitops', \  
'BMS', \  
'caTools', \  
'caret', \  
'codetools', \  
'colorRamps', \  
'classInt', \  
'data.table', \  
'dbplyr', \  
'evaluate', \  
'e1071', \  
'forecast', \  
'foreign', \  
'formatR', \  
'gdata', \  
'ggplot2', \  
'gridExtra', \  
'gstat', \  
'gtools', \  
'highr', \  
'knitr', \  
'leaflet', \  
'lubridate', \  
'lme4', \  
'magick', \  
'mapview', \  
'maptools', \  
'markdown', \  
'modules', \  
'network', \  
'nnet', \  
'plyr', \  
'plotrix', \  
'psych', \  
'randomForest', \  
'raster', \  
'rasterVis', \  
'readr', \  
'readxl', \  
'rgdal', \  
'rgeos', \  
'ROCR', \  
'rmarkdown', \  
'RPostgreSQL', \  
'rpart', \  
'rprojroot', \  
'servr', \  
'sf', \  
'shiny', \  
'SnowballC', \  
'sp', \  
'spdep', \  
'sphet', \  
'stargazer', \  
'stringr', \  
'tidyr', \  
'tidytext', \  
'tm', \  
'topicmodels', \  
'TOC', \  
'wordcloud', \  
'xts', \  
'zoo'))"  
# && Rscript -e "install.packages('rstan', \  
# repos = 'https://cloud.r-project.org/', \  
# configure.args = 'CXXFLAGS=-O3 -mtune=native -march=native -Wno-unused-
variable -Wno-unused-function -flto -ffat-lto-objects -Wno-unused-local-
typedefs -Wno-ignored-attributes -Wno-deprecated-declarations', \  
# dependencies = TRUE)"  
  
  
# Data & Configuration  
  
## For configuration of s6-overlay services (see root/etc/services.d)  
  
ADD root /  
  
## initialize postgresql, "student" role, and portal database  
  
RUN service postgresql start \  
&& su - postgres -c "psql -qc 'REVOKE ALL ON schema public FROM public'" \  
&& su - postgres -c "createdb portal" \  
&& su - postgres -c "createuser --no-login student" \  
&& su - postgres -c "psql portal -qc 'ALTER DEFAULT PRIVILEGES IN SCHEMA
public GRANT ALL ON TABLES TO student'" \  
&& su - postgres -c "psql portal -q < /var/backups/postgresql/portal_dump.sql"
\  
&& service postgresql stop \  
&& sed -e "s|\(127.0.0.1/32\s*\)md5|\1pam pamservice=postgresql96|" -i
/etc/postgresql/9.6/main/pg_hba.conf  
  
### FIXEME PostgreSQL on linux host  
### see https://github.com/docker/docker/issues/783#issuecomment-56013588  
RUN mkdir /etc/ssl/private-copy \  
&& mv /etc/ssl/private/* /etc/ssl/private-copy/ \  
&& rm -r /etc/ssl/private \  
&& mv /etc/ssl/private-copy /etc/ssl/private \  
&& chmod -R 0700 /etc/ssl/private \  
&& chown -R postgres /etc/ssl/private  
  
## create /home volume  
VOLUME /home  
  
ENV USER=""  
  
EXPOSE 80  
  
ENTRYPOINT ["/init"]  
  
## TODO  
# Check permissions on home directory  
# resolve makevar for root packages and this rstan thing  

