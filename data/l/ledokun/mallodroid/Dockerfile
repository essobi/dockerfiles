FROM alpine:3.6  
MAINTAINER Rom Luengwattanapong <s1567783@ed.ac.uk>  
  
USER root  
  
# Installs bash and php for run script  
RUN apk --no-cache upgrade \  
&& apk --no-cache add \  
bash \  
coreutils \  
php7 \  
php7-posix \  
php7-json  
  
# Installs Dependencies  
RUN apk --no-cache add --virtual .build-dependencies \  
ca-certificates \  
curl \  
git \  
openssl \  
tar \  
unzip \  
wget  
  
RUN apk --no-cache add --virtual .compile-dependencies \  
alpine-sdk \  
g++ \  
patch \  
&& apk --no-cache add \  
libxml2 \  
libxml2-dev \  
libxslt \  
libxslt-dev \  
musl-dev \  
py2-pip \  
python \  
python2-dev  
  
# Install Androguard and all its requirements  
RUN pip install --upgrade pip \  
&& pip install setuptools requests yara future \  
&& pip install git+git://github.com/dweinstein/pyfuzzy@master \  
&& pip install git+git://github.com/androguard/androguard.git@v2.0  
  
# Install Mallodroid  
ENV GIT_URL https://github.com/adithyabenny/mallodroid.git  
ENV MALLODROID_ROOT /opt/mallodroid/  
ENV PATH ${MALLODROID_ROOT}:$PATH  
RUN git clone ${GIT_URL} ${MALLODROID_ROOT}  
  
COPY mallodroid.patch ${MALLODROID_ROOT}  
  
RUN cd ${MALLODROID_ROOT} \  
&& patch < mallodroid.patch  
  
# Cleans up  
RUN apk del .build-dependencies .compile-dependencies \  
&& rm -rf /tmp/* /var/tmp/*  
  
# Create application folder  
RUN mkdir -p /app  
  
VOLUME ["/app"]  
  
COPY run.php /tmp/  
RUN chmod +x /tmp/run.php  
  
WORKDIR /tmp  
  
ENTRYPOINT ["/usr/bin/php", "/tmp/run.php"]  

