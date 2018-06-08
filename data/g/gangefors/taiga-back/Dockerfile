FROM python:3.5-slim  
MAINTAINER Stefan Gangefors <stefan@gangefors.com>  
  
ARG VERSION_REV=stable  
  
# Install build and runtime dependencies  
RUN buildDeps=' \  
build-essential \  
git \  
libjpeg-dev \  
libpq-dev \  
libxslt-dev \  
' && \  
runDeps=' \  
gettext \  
libjpeg62-turbo \  
libpq5 \  
libxslt1.1 \  
netcat \  
' \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps $runDeps \  
# Add taiga user and create home folder  
&& useradd -d /taiga -mU taiga \  
# Clone and install taiga-back requirements  
&& git clone https://github.com/taigaio/taiga-back.git /taiga/back \  
&& cd /taiga/back \  
&& git checkout $VERSION_REV \  
&& pip install --no-cache-dir -r requirements.txt \  
&& pip install --no-cache-dir circus gunicorn \  
# Remove build dependencies  
&& apt-get purge -y --auto-remove $buildDeps \  
&& rm -rf /var/lib/apt/lists/*  
  
# Configure taiga-back  
RUN mkdir -p /taiga/logs /taiga/media /taiga/static  
COPY local.py /taiga/back/settings/local.py  
COPY circus.ini /taiga/circus.ini  
COPY init /taiga/init  
  
VOLUME /taiga/logs  
VOLUME /taiga/media  
VOLUME /taiga/static  
  
EXPOSE 8000  
CMD ["/taiga/init"]  

