################################################################################  
# CORE Dockerfile  
# MAINTAINER airstack team <support@airstack.io>  
#  
# Conventions:  
#  
# RUN  
# - single command on one line  
# - multiple commands:  
# - `set -e; \\` on first line  
# - separate commands on subsequent lines, each ending with `; \\`  
#  
#  
################################################################################  
  
FROM debian:wheezy  
RUN echo "deb http://http.debian.net/debian wheezy-backports main" >>
/etc/apt/sources.list  
  
USER root  
ENV HOME /root  
WORKDIR /root  
RUN set -e; \  
groupadd --system airstack --gid 432; \  
useradd --uid 431 \--system \--base-dir /home --create-home --gid airstack
--shell /bin/nologin --comment "airstack user" airstack; \  
chown -R airstack:airstack /home/airstack  
################################################################################  
# PACKAGES  
#  
# Add commands required for installing packages. To minimize rebuilds,
binaries  
# that are modified less often should be in earlier RUN commands.  
#  
# Conventions:  
#  
# See Dockerfile.base conventions.  
#  
# Packages  
# - use core helper functions to install packages  
# - /command/core-package-install  
# - put development packages in Dockerfile.packages.development  
# - reserve this file for common packages only  
# - install packages to /package  
# - symlink commands in /package to /usr/bin or /usr/local/bin  
#  
################################################################################  
  
COPY core/build/ /package/airstack-0.1.0/build  
RUN set -e; \  
ln -s /package/airstack-0.1.0 /package/airstack; \  
chmod -R 1755 /package; \  
mkdir /command; \  
ln -s /package/airstack/build/core-* /command/  
  
# Packages::Base  
RUN set -e; \  
/command/core-package-install wget ca-certificates libssl1.0.0 libpcre3
openssl; \  
/command/core-slashpackage-install jq-1.4  
  
# Packages::runit  
RUN touch /etc/inittab && /command/core-package-install runit  
  
# Packages::socklog  
RUN /command/core-package-install socklog ipsvd netcat-openbsd  
  
# Packages::dropbear  
RUN /command/core-package-install dropbear  
  
# Packages::Lua  
RUN set -e; \  
/command/core-package-install luajit lua-posix; \  
mkdir -p /usr/local/share/lua/5.1; \  
ln -s /usr/bin/luajit /usr/bin/lua; \  
ln -s /package/airstack/core/lua/airstack.lua
/usr/local/share/lua/5.1/airstack.lua  
################################################################################  
# PACKAGES: DEVELOPMENT  
#  
# Add development packages here.  
################################################################################  
  
RUN set -e; \  
/command/core-package-install \  
ethtool net-tools \  
procps psmisc bwm-ng \  
sudo \  
man-db info \  
wget curl \  
inotify-tools \  
less vim-tiny; \  
ln -s /usr/bin/vim.tiny /usr/bin/vim  
  
RUN set -e; \  
/command/core-package-install \  
make bzip2  
################################################################################  
# SERVICES  
#  
# Add commands for configuring and managing services.  
#  
# Conventions:  
#  
# - do not install any packages in this file  
# - keep this file minimal to ensure faster rebuilds  
#  
################################################################################  
  
COPY core /package/airstack/core  
RUN ln -s /package/airstack/core/command/core-* /command/  
  
# socklog  
COPY services/socklog-unix /package/airstack/socklog-unix  
  
# runit  
COPY services/runit /package/airstack/runit  
RUN /package/airstack/runit/enable  
  
# dropbear  
COPY services/dropbear /package/airstack/dropbear  
EXPOSE 22  
################################################################################  
# SERVICES: DEVELOPMENT  
################################################################################  
  
# Password-less sudo enabled for airstack user  
RUN set -e; \  
echo "airstack ALL = NOPASSWD: ALL" > /etc/sudoers.d/airstack; \  
usermod --shell /bin/bash airstack  

