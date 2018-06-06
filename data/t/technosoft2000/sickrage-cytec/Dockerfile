FROM technosoft2000/alpine-base:3.6-3  
MAINTAINER Technosoft2000 <technosoft2000@gmx.net>  
LABEL image.version="1.1.4" \  
image.description="Docker image for SickRage, based on docker image of Alpine"
\  
image.date="2018-03-25" \  
url.docker="https://hub.docker.com/r/technosoft2000/sickrage-cytec" \  
url.github="https://github.com/Technosoft2000/docker-sickrage-cytec" \  
url.support="https://cytec.us/forum"  
# Set basic environment settings  
  
ENV \  
# - VERSION: the docker image version (corresponds to the above LABEL
image.version)  
VERSION="1.1.4" \  
# - PUSER, PGROUP: the APP user and group name  
PUSER="sickrage" \  
PGROUP="sickrage" \  
# - APP_NAME: the APP name  
APP_NAME="SickRage-Cytec" \  
# - APP_HOME: the APP home directory  
APP_HOME="/sickrage" \  
# - APP_REPO, APP_BRANCH: the APP GitHub repository and related branch  
# for related branch or tag use e.g. master, develop, ...  
APP_REPO="https://github.com/cytec/SickRage.git" \  
APP_BRANCH="master" \  
# - SYNO_VOLUME: Snyology NAS volume main directory  
SYNO_VOLUME="/volume1" \  
# - PKG_*: the needed applications for installation  
PKG_DEV="make gcc g++" \  
PKG_DEV_KEEP="python-dev openssl-dev libffi-dev" \  
PKG_PYTHON="ca-certificates py-pip python py-libxml2 py-lxml" \  
PKG_COMPRESS="unrar"  
  
RUN \  
# create temporary directories  
mkdir -p /tmp && \  
mkdir -p /var/cache/apk && \  
# update the package list  
apk -U upgrade && \  
# install the needed applications  
apk -U add --no-cache $PKG_DEV $PKG_DEV_KEEP $PKG_PYTHON $PKG_COMPRESS && \  
# install additional python packages:  
# setuptools, pyopenssl, cheetah, requirements  
pip --no-cache-dir install --upgrade pip && \  
pip --no-cache-dir install --upgrade setuptools && \  
pip --no-cache-dir install --upgrade pyopenssl cheetah requirements requests
&& \  
# remove not needed packages  
apk del $PKG_DEV && \  
# create Snyology NAS /volume1 folders  
# to easily provide the same corresponding host directories at the APP  
mkdir -p $SYNO_VOLUME/downloads && \  
mkdir -p $SYNO_VOLUME/video && \  
mkdir -p $SYNO_VOLUME/certificates && \  
# create the APP folder structure  
mkdir -p $APP_HOME/app && \  
mkdir -p $APP_HOME/config && \  
mkdir -p $APP_HOME/data && \  
# cleanup temporary files  
rm -rf /tmp && \  
rm -rf /var/cache/apk/*  
  
# set the working directory for the APP  
WORKDIR $APP_HOME/app  
  
#start.sh will download the latest version of the APP and run it.  
COPY *.txt /init/  
COPY *.sh /init/  
# Set volumes for the APP folder structure  
VOLUME $APP_HOME/config $APP_HOME/data $SYNO_VOLUME/downloads
$SYNO_VOLUME/video $SYNO_VOLUME/certificates  
  
# Expose ports  
EXPOSE 8081  

