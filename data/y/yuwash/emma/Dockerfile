# opencv-dev only available in edge  
FROM alpine:edge  
  
LABEL maintainer "YWashio at EONERC.RWTH-Aachen.de"  
  
RUN echo 'http://dl-cdn.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories  
RUN apk update  
RUN apk add --no-cache \  
build-base \  
qt5-qtbase-dev \  
git  
RUN apk add --no-cache \  
opencv-dev  
RUN apk add --no-cache \  
cmake \  
bluez-dev  
RUN ln -s qmake-qt5 /usr/bin/qmake  

