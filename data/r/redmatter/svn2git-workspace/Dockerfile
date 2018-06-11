FROM debian:jessie  
  
MAINTAINER Dino.Korah@redmatter.com  
  
ENV TZ="Europe/London" \  
EDITOR="/usr/bin/vim" \  
TERM="linux" \  
SHELL="/bin/bash" \  
WORKSPACE="/workspace"  
RUN ( \  
export DEBIAN_FRONTEND=noninteractive; \  
export BUILD_DEPS=""; \  
export APP_DEPS="openssh-client subversion git-core git-svn ruby rubygems vim-
nox xmlstarlet"; \  
  
set -e -u -x; \  
  
apt-get update; \  
apt-get -y upgrade; \  
apt-get install -y --no-install-recommends ${APP_DEPS} ${BUILD_DEPS}; \  
  
gem install svn2git; \  
  
apt-get remove -y $BUILD_DEPS; \  
apt-get clean autoclean; \  
apt-get autoremove --yes; \  
rm -rf /var/lib/{apt,dpkg,cache,log}/; \  
)  
  
COPY get-authors.sh /usr/bin/get-authors  
  
WORKDIR $WORKSPACE  

