FROM comses/miracle-base  
  
ARG MRO_VERSION=3.3.1  
ARG MRO_FILE=microsoft-r-open-$MRO_VERSION.tar.gz  
ARG
MRO_URL=https://mran.revolutionanalytics.com/install/mro/$MRO_VERSION/$MRO_FILE  
  
RUN yum -y install epel-release && yum makecache && yum -y install wget
postgresql-devel libffi-devel libicu-devel \  
pango-devel librsvg2-devel zlib-devel libcurl-devel gcc gcc-c++ gcc-gfortran
make openssl-devel \  
libquadmath-devel libstdc++-devel libquadmath libgfortran ed gettext-devel
glibc-devel glibc-headers unzip \  
&& wget -q $MRO_URL && tar zxf $MRO_FILE && cd microsoft-r-open && sh
install.sh -u -a \  
&& R -e "install.packages(c('shiny', 'rmarkdown',
'data.table','raster','rasterVis', 'sqldf', 'lattice', 'latticeExtra',
'RPostgreSQL', 'devtools'))" \  
&& R -e "devtools::install_github('kevinushey/sourcetools')" \  
&& R -e "install.packages('radiant', repos='https://radiant-
rstats.github.io/minicran/')" \  
&& rm -f /$MRO_FILE && yum clean all  

