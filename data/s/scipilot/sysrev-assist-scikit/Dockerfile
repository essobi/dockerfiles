# This is the intermediate image for the SciKit Learn requirements for SysRev
Doc API  
# https://hub.docker.com/r/scipilot/sysrev-assist-scikit  
#  
#  
# Notes:  
# These reduce the overall image size:  
# apk --no-cache  
# apk --virtual .build-deps and then apk del .build-deps : stuff needed for
only install but not for execution later.  
# clean up build artefacts, within the same RUN - to reduce file layers  
# pip install --no-cache-dir  
# docker build --squash  
FROM python:3.6-alpine3.7  
  
# Package dependencies  
# Scipy needs quite a few specific packages set up carefully...  
# the lapack package is only in the community repository  
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories  
RUN apk --update add --no-cache \  
lapack-dev \  
gcc \  
freetype-dev \  
python3-dev  
  
RUN apk add --no-cache --virtual .build-deps gfortran musl-dev g++ && \  
ln -s /usr/include/locale.h /usr/include/xlocale.h && \  
# I found installing numpy and scipy separately from SKLearn solved issues
with its setup (i.e. it doesn't work from requirements.txt)  
pip install numpy==1.14 && \  
pip install scipy==1.0 && \  
pip install scikit-learn==0.19 && \  
apk del .build-deps

