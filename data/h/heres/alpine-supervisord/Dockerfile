FROM alpine:3.4  
MAINTAINER Lukasz Kaczynski <heres@devoft.pl>  
  
ENV PYTHON_VERSION=3.5.2-r2  
ENV SUPERVISOR_VERSION=3.3.0  
ENV POSTGRESQL_CLIENT_VERSION=9.5.4-r0  
ENV BUILD_PACKAGES="\  
build-base \  
linux-headers \  
python3-dev \  
libjpeg-turbo-dev \  
tiff-dev \  
zlib-dev \  
"  
RUN apk update && \  
apk add -u --no-cache \  
bash supervisor libjpeg-turbo tiff zlib \  
ncurses \  
python3=$PYTHON_VERSION \  
postgresql-client=$POSTGRESQL_CLIENT_VERSION postgresql-
dev==$POSTGRESQL_CLIENT_VERSION \  
$BUILD_PACKAGES python ca-certificates && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install -U pip setuptools && pip3 install incremental==16.10.1 twisted
wheel daphne psycopg2 pillow posix-ipc && \  
apk del $BUILD_PACKAGES python && \  
ln -sf /usr/bin/python3 /usr/local/bin/python && \  
find /usr -name *.pyc -delete || echo "OKi" && \  
rm -r /root/.cache  
  
ENTRYPOINT ["supervisord", "--nodaemon", "--configuration",
"/etc/supervisord.conf"]  
  

