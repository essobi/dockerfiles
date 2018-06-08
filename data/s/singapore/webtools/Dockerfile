FROM ubuntu:16.04  
  
WORKDIR /src  
  
# BASE  
  
RUN \  
apt-get -y update && \  
apt-get -y --no-install-recommends install \  
wget \  
curl \  
build-essential \  
zip \  
unzip \  
dos2unix \  
git \  
xml-twig-tools \  
software-properties-common && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# NODE  
  
RUN \  
curl -sL https://deb.nodesource.com/setup_7.x | bash - && \  
apt-get -y --no-install-recommends install nodejs && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# PYTHON  
  
RUN \  
apt-get -y update && \  
apt-get -y --no-install-recommends install \  
python-pip \  
python-yaml \  
python-dev \  
libffi-dev \  
libxml2-dev \  
libxslt-dev \  
lib32z1-dev \  
libssl-dev \  
python-software-properties \  
firefox \  
xvfb && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN pip install -U pip setuptools  
  
RUN \  
pip install flo scrapy csvkit pyasn1 service_identity twisted awscli
beautifulsoup4 selenium pyvirtualdisplay --upgrade && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# npm globals  
  
RUN npm install -g mapshaper svgo  
  
# R  
  
RUN \  
add-apt-repository -y ppa:marutter/rrutter && \  
apt-get -y update && \  
apt-get -y --no-install-recommends install \  
r-base \  
r-base-dev \  
r-cran-plyr \  
libcairo2-dev \  
libxt-dev \  
python-all-dev \  
libpq-dev \  
libgeos-dev \  
libgdal1-dev \  
libproj-dev && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN echo
'install.packages(c("sp","rgdal","TeachingDemos","Cairo","rgeos","RPostgreSQL"),repos="http://cran.rstudio.com",quiet=FALSE)'
>> install.r && \  
echo 'install.packages("doSNOW", repo="http://cran.us.r-project.org")' >>
install.r && \  
echo 'install.packages("plotrix", repo="http://cran.us.r-project.org")' >>
install.r && \  
Rscript install.r  
  
# POSTGIS  
  
RUN \  
echo "deb http://apt.postgresql.org/pub/repos/apt xenial-pgdg main" >>
/etc/apt/sources.list && \  
wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | apt-
key add - && \  
apt-get update -y && \  
apt-get -y --no-install-recommends install postgresql-9.6-postgis-2.2
postgresql-contrib-9.6 postgis && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV PSQL "psql -h localhost -U postgres -v ON_ERROR_STOP=1"  
  
# S3CMD  
  
RUN \  
wget -O- -q http://s3tools.org/repo/deb-all/stable/s3tools.key | apt-key add -
&& \  
wget -O/etc/apt/sources.list.d/s3tools.list http://s3tools.org/repo/deb-
all/stable/s3tools.list && \  
apt-get update -y && \  
apt-get install -y s3cmd && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

