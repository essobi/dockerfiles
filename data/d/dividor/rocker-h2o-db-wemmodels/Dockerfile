#  
# Main rocker image, extended for H2O.AI, rJava, Microsoft SQL server 11 ODBC,
text2vec, word2vector,  
# plus a bunch of other R packages  
#  
  
FROM rocker/tidyverse:latest  
  
# Install Unix ODBC (for RODBC)  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
unixODBC \  
pkg-config \  
libltdl7 \  
libodbc1 \  
unixodbc-dev  
  
# Java 8  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" \  
| tee /etc/apt/sources.list.d/webupd8team-java.list \  
&& echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main"
\  
| tee -a /etc/apt/sources.list.d/webupd8team-java.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
\  
&& echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true" \  
| /usr/bin/debconf-set-selections \  
&& apt-get update \  
&& apt-get install -y oracle-java8-installer \  
&& update-alternatives --display java \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean  
RUN R CMD javareconf  
  
# Need these if using rJava  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
liblzma-dev \  
libicu-dev \  
libbz2-dev \  
libpcre3-dev  
  
# Install additional useful R packages  
RUN echo 'install.packages(c("RODBC", \  
"dplyr", \  
"reshape2", \  
"h2o", \  
"memoise", \  
"plotly", \  
"devtools", \  
"text2vec", \  
"ReporteRs", \  
"sqldf", \  
"plyr", \  
"tidyr", \  
"ggplot2", \  
"splitstackshape", \  
"rJava", \  
"tm", \  
"tsne", \  
"ape"), \  
repos="http://cran.us.r-project.org", dependencies=TRUE)' > /tmp/packages.R \  
&& Rscript /tmp/packages.R  
  
# Install word2vectors  
RUN echo 'library(devtools); \  
install_github("bmschmidt/wordVectors")' > /tmp/packages.R \  
&& Rscript /tmp/packages.R  
  
# Install text2vec, which has LDA, LSA and Glove  
# https://cran.r-project.org/web/packages/text2vec/index.html  
RUN echo 'install.packages(c("text2vec"), \  
repos="http://cran.us.r-project.org", dependencies=TRUE)' > /tmp/packages.R \  
&& Rscript /tmp/packages.R  
  
# SQL server horribleness - 11 ODBC. Hopefully we can get a standard
deployment when rocker update  
# their Linux version.  
RUN cd  
RUN wget
http://download.microsoft.com/download/B/C/D/BCDD264C-7517-4B7D-8159-C99FC5535680/RedHat6/msodbcsql-11.0.2270.0.tar.gz  
RUN tar xf msodbcsql-11.0.2270.0.tar.gz  
WORKDIR "msodbcsql-11.0.2270.0"  
RUN pwd  
RUN rm install.sh build_dm.sh  
RUN wget https://raw.githubusercontent.com/tax/mssqldriver/master/install.sh  
RUN wget https://raw.githubusercontent.com/tax/mssqldriver/master/build_dm.sh  
RUN bash install.sh install --accept-license --force  
RUN rm /usr/lib/x86_64-linux-gnu/libodbcinst.so.1  
RUN rm /usr/lib/x86_64-linux-gnu/libodbc.so.1  
RUN ln -s /usr/lib/x86_64-linux-gnu/libodbcinst.so.2.0.0
/usr/lib/x86_64-linux-gnu/libodbcinst.so.1 ;  
RUN ln -s /lib/x86_64-linux-gnu/libodbc.so.2.0.0 /usr/lib/x86_64-linux-
gnu/libodbc.so.1;  
RUN ln -s /usr/lib/x86_64-linux-gnu/libcrypto.so.1.0.0 /usr/lib/x86_64-linux-
gnu/libcrypto.so.10;  
RUN ln -s /usr/lib/x86_64-linux-gnu/libssl.so.1.0.0 /usr/lib/x86_64-linux-
gnu/libssl.so.10;  

