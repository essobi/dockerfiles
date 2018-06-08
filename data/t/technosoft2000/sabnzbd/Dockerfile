FROM technosoft2000/alpine-base:3.6-3  
MAINTAINER Technosoft2000 <technosoft2000@gmx.net>  
LABEL image.version="1.1.8" \  
image.description="Docker image for SABnzbd, based on docker image of Alpine"
\  
image.date="2018-03-25" \  
url.docker="https://hub.docker.com/r/technosoft2000/sabnzbd" \  
url.github="https://github.com/Technosoft2000/docker-sabnzbd" \  
url.support="https://cytec.us/forum"  
# Set basic environment settings  
ENV \  
# - VERSION: the docker image version (corresponds to the above LABEL
image.version)  
VERSION="1.1.8" \  
# - PUSER, PGROUP: the APP user and group name  
PUSER="sabnzbd" \  
PGROUP="sabnzbd" \  
# - APP_NAME: the APP name  
APP_NAME="SABnzbd" \  
# - APP_HOME: the APP home directory  
APP_HOME="/sabnzbd" \  
# - APP_REPO, APP_BRANCH: the APP GitHub repository and related branch  
# for related branch or tag use e.g. master, 0.7.x, 1.0.x, 1.1.x, 1.2.x,
2.0.x, develop, ...  
APP_REPO="https://github.com/sabnzbd/sabnzbd.git" \  
APP_BRANCH="master" \  
# - DOWNLOADS: main download folder  
DOWNLOADS="/downloads" \  
# - NZBTOMEDIA_REPO, NZBTOMEDIA_BRANCH: nzbToMedia GitHub repository and
related branch  
NZBTOMEDIA_REPO="https://github.com/clinton-hall/nzbToMedia.git" \  
NZBTOMEDIA_BRANCH="master" \  
# - PKG_*: the needed applications for installation  
PKG_DEV="make gcc g++ automake autoconf" \  
PKG_DEV_KEEP="python-dev openssl-dev libffi-dev libgomp" \  
PKG_PYTHON="ca-certificates py2-pip python py-libxml2 py-lxml" \  
PKG_COMPRESS="unrar unzip tar p7zip" \  
PKG_ADDONS="ffmpeg" \  
# - PAR2_*: par2commandline GitHub repository and related branch  
# for related branch or tag use e.g. master, ..., v0.6.14, v0.7.0, v0.7.1, ...  
PAR2_REPO="https://github.com/Parchive/par2cmdline.git" \  
PAR2_BRANCH="v0.8.0"  
  
RUN \  
# create temporary directories  
mkdir -p /tmp && \  
mkdir -p /var/cache/apk && \  
# update the package list  
apk -U upgrade && \  
# install the needed applications  
apk -U add --no-cache $PKG_DEV $PKG_DEV_KEEP $PKG_PYTHON $PKG_COMPRESS
$PKG_ADDONS && \  
# install par2  
git clone -b $PAR2_BRANCH --single-branch --depth 1 $PAR2_REPO && \  
cd /par2cmdline && \  
aclocal && \  
automake --add-missing && \  
autoconf && \  
./configure && \  
make && \  
make check && \  
make install && \  
cd / && \  
rm -rf par2cmdline && \  
# install additional python packages:  
# setuptools, pyopenssl, cheetah, requirements  
pip --no-cache-dir install --upgrade pip && \  
pip --no-cache-dir install --upgrade setuptools && \  
pip --no-cache-dir install --upgrade pyopenssl cheetah requirements requests
&& \  
pip --no-cache-dir install --upgrade sabyenc cryptography && \  
#pip install http://www.golug.it/pub/yenc/yenc-0.4.0.tar.gz && \  
# remove not needed packages  
apk del $PKG_DEV && \  
# create the APP folder structure  
mkdir -p $APP_HOME/app && \  
mkdir -p $APP_HOME/nzbbackups && \  
mkdir -p $APP_HOME/config && \  
mkdir -p $APP_HOME/config/scripts && \  
mkdir -p $DOWNLOADS/complete && \  
mkdir -p $DOWNLOADS/incomplete && \  
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
VOLUME $APP_HOME/config $APP_HOME/nzbbackups $DOWNLOADS/complete
$DOWNLOADS/incomplete  
  
# Expose ports  
EXPOSE 8080 9090  

