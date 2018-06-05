# Dockerfile for CALDB  
# http://cxc.cfa.harvard.edu/ciao/download/caldb.html  
FROM ubuntu:15.10  
MAINTAINER ldouchy  
  
# Prerequisite packages installation & clean  
RUN apt-get update \  
&& apt-get install -y \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
# caldbmgr:caldb user creation  
RUN mkdir /opt/CALDB \  
&& groupadd caldb && useradd -r -g caldb caldbmgr \  
&& chown caldbmgr:caldb /opt/CALDB  
  
# switch to user caldbmgr  
USER caldbmgr  
  
workdir /opt/CALDB  
  
ENV CALDB_VERSION=4.6.9 \  
ACIS_VERSION=4.6.9 \  
HRC_VERSION=4.6.1.1  
# Download, Untar, Remove  
RUN wget
ftp://cda.harvard.edu/pub/arcftp/caldb/caldb_${CALDB_VERSION}_main.tar.gz \  
&& tar xzvf caldb_${CALDB_VERSION}_main.tar.gz \  
&& rm -f caldb_${CALDB_VERSION}_main.tar.gz  
RUN wget
ftp://cda.harvard.edu/pub/arcftp/caldb/acis_bkgrnd_${ACIS_VERSION}.tar.gz \  
&& tar xzvf acis_bkgrnd_${ACIS_VERSION}.tar.gz \  
&& rm -f acis_bkgrnd_${ACIS_VERSION}.tar.gz  
RUN wget
ftp://cda.harvard.edu/pub/arcftp/caldb/hrc_bkgrnd_${HRC_VERSION}.tar.gz \  
&& tar xzvf hrc_bkgrnd_${HRC_VERSION}.tar.gz \  
&& rm -f hrc_bkgrnd_${HRC_VERSION}.tar.gz  
# Documentation  
RUN wget
ftp://cda.harvard.edu/pub/arcftp/caldb/README_caldb${CALDB_VERSION}.txt \  
&& wget
ftp://cda.harvard.edu/pub/arcftp/caldb/MANIFEST_${CALDB_VERSION}_main.txt  
  
# reset user for next layer  
USER root  

