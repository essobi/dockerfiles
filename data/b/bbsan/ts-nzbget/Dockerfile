FROM technosoft2000/alpine-base:3.6-2  
MAINTAINER bbsan <bbsan@gmx.de>  
LABEL image.version="1.0" \  
image.description="Docker image for nzbget, based on docker image of Alpine" \  
image.date="2017-06-04" \  
url.docker="https://hub.docker.com/r/bbsan/ts-nzbget" \  
url.github="https://github.com/bbsan2k/ts-nzbget" \  
url.support="https://cytec.us/forum"  
  
ARG NZBGET_BRANCH="stable"  
# Set basic environment settings  
ENV \  
# - VERSION: the docker image version (corresponds to the above LABEL
image.version)  
VERSION="1.0" \  
# - PUSER, PGROUP: the APP user and group name  
PUSER="nzbget" \  
PGROUP="nzbget" \  
# - APP_NAME: the APP name  
APP_NAME="nzbget" \  
# - APP_HOME: the APP home directory  
APP_HOME="/nzbget" \  
# - DOWNLOADS: main download folder  
DOWNLOADS="/downloads" \  
# NZBGET_BRANCH  
NZBGET_CHANNEL="stable" \  
# - NZBTOMEDIA_REPO, NZBTOMEDIA_BRANCH: nzbToMedia GitHub repository and
related branch  
NZBTOMEDIA_REPO="https://github.com/clinton-hall/nzbToMedia.git" \  
NZBTOMEDIA_BRANCH="master" \  
# - MP4_AUTOMATOR_REPO, MP4_AUTOMATOR_BRANCH: mp4_automator GitHub repository
and related branch  
MP4_AUTOMATOR_REPO="https://github.com/mdhiggins/sickbeard_mp4_automator.git"
\  
MP4_AUTOMATOR_BRANCH="master" \  
# - PKG_*: the needed applications for installation  
PKG_DEV="make gcc g++ automake autoconf python-dev openssl-dev libffi-dev" \  
PKG_DOWNLOAD="curl wget" \  
PKG_PYTHON="ca-certificates py2-pip python2 py-libxml2 py-lxml" \  
PKG_COMPRESS="unrar unzip tar p7zip bzip2 zlib xz tar" \  
PKG_ADDONS="ffmpeg"  
  
RUN \  
# create temporary directories  
mkdir -p /tmp && \  
mkdir -p /var/cache/apk && \  
# update the package list  
apk -U upgrade && \  
# install the needed applications  
apk -U add --no-cache $PKG_DEV $PKG_DOWNLOAD $PKG_PYTHON $PKG_COMPRESS
$PKG_ADDONS && \  
# install additional python packages:  
# setuptools, pyopenssl, cheetah, requirements  
pip --no-cache-dir install --upgrade pip && \  
pip --no-cache-dir install --upgrade setuptools && \  
pip --no-cache-dir install --upgrade pyopenssl cheetah requirements requests
babelfish && \  
# remove not needed packages  
apk del $PKG_DEV && \  
# create the APP folder structure  
mkdir -p $APP_HOME/app && \  
mkdir -p $APP_HOME/config && \  
mkdir -p $APP_HOME/scripts && \  
mkdir -p $DOWNLOADS/complete && \  
mkdir -p $DOWNLOADS/incomplete && \  
# install nzbget  
curl -o \  
/nzbget/versions.json -L \  
http://nzbget.net/info/nzbget-version-linux.json && \  
NZBGET_VERSION=$(grep "${NZBGET_CHANNEL}-download" /nzbget/versions.json | cut
-d '"' -f 4) && \  
curl -o \  
/tmp/nzbget.run -L \  
"${NZBGET_VERSION}" && \  
sh /tmp/nzbget.run --destdir /nzbget/app && \  
  
# cleanup temporary files  
rm -rf /tmp && \  
rm -rf /var/cache/apk/*  
  
# set the working directory for the APP  
WORKDIR $APP_HOME/app  
  
# copy files to the image (info.txt and scripts)  
COPY *.txt /init/  
COPY *.sh /init/  
  
# set the working directory of the APP  
WORKDIR $APP_HOME/app  
  
# Set volumes for the the APP folder structure  
VOLUME $APP_HOME/config $DOWNLOADS  
  
# Expose ports  
EXPOSE 6789

