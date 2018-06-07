# Copyright 2015-2016 jitakirin  
#  
# This file is part of docker-rpmbuild.  
#  
# docker-rpmbuild is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
#  
# docker-rpmbuild is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with docker-rpmbuild. If not, see <http://www.gnu.org/licenses/>.  
# Based on: http://fedoraproject.org/wiki/How_to_create_an_RPM_package  
# And also:  
# - https://registry.hub.docker.com/u/nishigori/rpmbuild  
# - https://registry.hub.docker.com/u/sydneyuni/rpm-build-env/  
FROM i386/centos:6 as busybox  
  
RUN echo "i686" > /etc/yum/vars/arch && \  
echo "i386" > /etc/yum/vars/basearch  
  
RUN yum install -y gcc && \  
yum clean all -y && \  
rm -r -f /var/cache/*  
  
# busybox build based on:  
# https://github.com/docker-
library/busybox/blob/d24edba7ceb0033e2b28215f5e8a89ebb419f322/glibc/Dockerfile.builder  
ENV BUSYBOX_VERSION 1.28.1  
RUN set -ex; \  
cd /tmp; \  
tarball="busybox-${BUSYBOX_VERSION}.tar.bz2"; \  
curl -fL -o busybox.tar.bz2 "https://busybox.net/downloads/$tarball"; \  
mkdir -p /usr/src/busybox; \  
tar -xf busybox.tar.bz2 -C /usr/src/busybox --strip-components 1; \  
rm busybox.tar.bz2*  
  
WORKDIR /usr/src/busybox  
  
RUN set -ex; \  
\  
setConfs=' \  
CONFIG_WGET=y \  
CONFIG_FEATURE_WGET_STATUSBAR=y \  
CONFIG_FEATURE_WGET_TIMEOUT=y \  
CONFIG_FEATURE_WGET_HTTPS=y \  
'; \  
\  
make allnoconfig; \  
\  
for confV in $setConfs; do \  
conf="${confV%=*}"; \  
sed -i \  
-e "s!^$conf=.*\$!$confV!" \  
-e "s!^# $conf is not set\$!$confV!" \  
.config; \  
if ! grep -q "^$confV\$" .config; then \  
echo "$confV" >> .config; \  
fi; \  
done; \  
\  
make oldconfig; \  
\  
# trust, but verify  
for confV in $setConfs; do \  
grep -q "^$confV\$" .config; \  
done;  
  
RUN set -ex \  
&& make -j "$(nproc)" \  
busybox  
  
FROM toopher/centos-i386:centos5  
MAINTAINER Michael Gliwinski <michael.gliwinski@henderson-group.com>  
  
RUN sed -i -re 's/^\s*(mirrorlist)/#\1/' /etc/yum.repos.d/CentOS-*.repo && \  
sed -i -re \  
's,#\s*(baseurl.*)mirror.centos.org/centos/(\$releasever|5),\1vault.centos.org/5.11,'
\  
/etc/yum.repos.d/CentOS-*.repo  
RUN linux32 yum install -y epel-release && \  
linux32 yum install -y rpmdevtools yum-utils buildsys-macros && \  
linux32 yum clean all && \  
linux32 rm -r -f /var/cache/*  
ADD docker-init.sh docker-rpm-build.sh /usr/local/bin/  
COPY \--from=busybox /usr/src/busybox/busybox /usr/local/bin/wget  
RUN chmod +x /usr/local/bin/*  
  
RUN linux32 useradd rpmbuild  
USER rpmbuild  
RUN linux32 rpmdev-setuptree  
USER root  
  
ENTRYPOINT ["linux32", "/usr/local/bin/docker-init.sh"]  

