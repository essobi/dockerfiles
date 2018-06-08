FROM debian:9-slim  
  
# Set environment vars  
ENV DEBIAN_FRONTEND=noninteractive \  
LANG=en_US.UTF-8 \  
LC_ALL=C.UTF-8 \  
LANGUAGE=en_US.UTF-8 \  
APP_DIR=/app \  
SIEGE_VERSION=4.0.4  
# Create app dir  
RUN mkdir -p ${APP_DIR}  
WORKDIR ${APP_DIR}  
  
# Install and build Siege from source  
RUN set -ex && \  
buildDeps=' \  
build-essential \  
libssl-dev \  
curl \  
zlib1g-dev \  
' && \  
runDeps=' \  
ca-certificates \  
libssl1.0.2 \  
' && \  
apt-get update && \  
apt-get install -y --no-install-recommends $buildDeps $runDeps && \  
curl -O http://download.joedog.org/siege/siege-${SIEGE_VERSION}.tar.gz && \  
tar -xvzf siege-${SIEGE_VERSION}.tar.gz && \  
cd siege-${SIEGE_VERSION} && \  
./configure && \  
make && \  
make install && \  
cd ${APP_DIR} && \  
apt-get purge -y --auto-remove $buildDeps && \  
rm -rf /var/lib/apt/lists/* ${APP_DIR}/siege-${SIEGE_VERSION}*  
  
# Copy siege files  
COPY . ${APP_DIR}/  
COPY siege.conf /root/.siege/siege.conf  
  
# App command  
ENTRYPOINT [ "/usr/local/bin/siege" ]  
CMD [ "--help" ]  

