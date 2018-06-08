#  
# PostgreSQL server and extensions docker image  
#  
# http://github.com/tenstartups/postgresql-docker  
#  
FROM postgres:alpine  
  
LABEL maintainer="Marc Lennox <marc.lennox@gmail.com>"  
  
# Set environment.  
ENV \  
LZOP_VERSION=1.03 \  
PV_VERSION=1.6.0  
# Install base packages.  
RUN \  
apk --update add build-base git lzo-dev nano python3-dev py2-pip wget && \  
rm -rf /var/cache/apk/*  
  
# Install lzop from source.  
RUN \  
wget https://www.lzop.org/download/lzop-${LZOP_VERSION}.tar.gz -O
/tmp/lzop-${LZOP_VERSION}.tar.gz && \  
tar xvfz /tmp/lzop-${LZOP_VERSION}.tar.gz -C /tmp && \  
cd /tmp/lzop-${LZOP_VERSION} && \  
wget -q -O - "https://raw.githubusercontent.com/openembedded/openembedded-
core/master/meta/recipes-support/lzop/lzop/lzop-1.03-gcc6.patch" | git apply
-v && \  
./configure && \  
make && \  
make install && \  
cd / && \  
rm -r /tmp/lzop-${LZOP_VERSION}*  
  
# Install pv from source.  
RUN \  
wget http://www.ivarch.com/programs/sources/pv-${PV_VERSION}.tar.bz2 -O
/tmp/pv-${PV_VERSION}.tar.bz2 && \  
tar xvfj /tmp/pv-${PV_VERSION}.tar.bz2 -C /tmp && \  
cd /tmp/pv-${PV_VERSION} && \  
./configure && \  
make && \  
make install && \  
cd / && \  
rm -r /tmp/pv-${PV_VERSION}*  
  
# Update pip version.  
RUN pip3 install --upgrade pip  
  
# Add Heroku WAL-E tools for postgres WAL archiving.  
RUN pip3 install boto wal-e  
  
# Copy the new entrypoint script into place.  
RUN mv /docker-entrypoint.sh /docker-entrypoint-orig.sh  
COPY entrypoint.sh /docker-entrypoint.sh  

