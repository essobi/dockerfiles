FROM alpine:edge  
MAINTAINER Nando Sola <nando@graphenedb.com>  
  
ENV LANG C.UTF-8  
ENV ARCH amd64  
  
# 'gosu' wil be used instead of 'sudo', as recommended by:  
# http://docs.docker.com/articles/dockerfile_best-practices/  
ENV GOSU_VERSION 1.10  
ENV GOSU_SHA256_SUM
5b3b03713a888cee84ecbf4582b21ac9fd46c3d935ff2d7ea25dd5055d302d3c  
  
#==================================================  
# Miscellaneous packages  
# Add required CircleCI tools:  
# https://circleci.com/docs/2.0/custom-images/#required-tools  
#==================================================  
RUN apk add --no-cache \  
shadow \  
ca-certificates \  
tar bzip2 zip unzip \  
wget curl \  
bash openssh-client \  
secure-delete \  
git python2  
  
# ========================================================================  
# Download a precompiled binary for gosu (https://github.com/tianon/gosu)  
# ========================================================================  
RUN wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$ARCH" &&
\  
echo "$GOSU_SHA256_SUM /usr/local/bin/gosu" | sha256sum -c - && \  
chmod 4755 /usr/local/bin/gosu  
  
# Fake sudo, as a wrapper for gosu  
ADD bin/fakesudo /usr/local/bin/sudo  
RUN chmod 755 /usr/local/bin/sudo  
  

