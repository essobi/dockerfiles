FROM alpine:latest  
LABEL maintainer="Christian Wagner https://github.com/chriswayg"  
ENV TERM="xterm"  
ENV S3QL_CACHE_DIR="/root/.s3ql"  
ENV S3QL_AUTHINFO_FILE="/root/.s3ql/authinfo2"  
ENV S3QL_MOUNT_OPTIONS="--allow-other"  
ENV S3QL_MOUNTPOINT="/mnt/s3ql"  
ENV S3QL_PREFIX="default"  
ENV S3QL_CRONTAB="@daily echo 'No backup command has been set!'"  
ENV
SUPERCRONIC_URL=https://github.com/aptible/supercronic/releases/download/v0.1.5/supercronic-
linux-amd64  
ENV SUPERCRONIC_SHA1SUM=9aeb41e00cc7b71d30d33c57a2333f2c2581a201  
  
# Install dependencies.  
RUN apk --no-cache add --update \  
coreutils \  
util-linux \  
tar \  
psmisc \  
procps \  
openssl \  
rsync \  
python3 \  
fuse \  
sqlite-libs \  
build-base \  
python3-dev \  
attr-dev \  
fuse-dev \  
sqlite-dev \  
# Upgrade pip and install Python module dependencies  
&& pip3 install --upgrade pip \  
&& pip3 install pycrypto defusedxml requests apsw llfuse dugong setuptools
pytest \  
&& cd /tmp \  
# Determine latest version of s3ql and download source code  
&& S3QL_VERSION=$(wget -q
https://bitbucket.org/nikratio/s3ql/raw/default/Changes.txt -O - | grep -m1
"20" | sed 's/.*\\([0-9].[0-9][0-9]\\)/\1/') \  
&& echo "*** Downloading S3QL Version: ${S3QL_VERSION}" \  
&& wget -q
https://bitbucket.org/nikratio/s3ql/downloads/s3ql-${S3QL_VERSION}.tar.bz2 \  
&& tar jxf s3ql-${S3QL_VERSION}.tar.bz2 \  
&& cd /tmp/s3ql-${S3QL_VERSION} \  
# Build s3ql and run tests  
&& python3 setup.py build_ext --inplace \  
&& mkdir -pv /root/.s3ql/ \  
&& python3 -m pytest -rs tests/ \  
# Install s3ql in /usr  
&& python3 setup.py install \  
# Remove build related stuff  
&& pip3 uninstall -y pytest \  
&& apk del build-base python3-dev attr-dev fuse-dev sqlite-dev \  
&& rm -r /tmp/s3ql-* \  
&& echo -e "*** Installed \c" \  
&& mount.s3ql --version \  
# Add cron for containers  
&& wget -q -O /usr/local/bin/supercronic ${SUPERCRONIC_URL} \  
&& echo "${SUPERCRONIC_SHA1SUM} /usr/local/bin/supercronic" | sha1sum -c - \  
&& chmod +x /usr/local/bin/supercronic  
  
# Copy docker-entrypoint, s3ql  
COPY ./scripts/ /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint"]  

