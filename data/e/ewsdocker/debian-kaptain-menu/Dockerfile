# =========================================================================  
# =========================================================================  
#  
# Dockerfile  
# Dockerfile for kaptain-menu-debian in a Debian-based docker container.  
#  
# =========================================================================  
#  
# @author Jay Wheeler.  
# @version 1.0.3  
# @copyright © 2017, 2018. EarthWalk Software.  
# @license Licensed under the GNU General Public License, GPL-3.0-or-later.  
# @package ewsdocker/debian-kaptain-menu  
# @subpackage Dockerfile  
#  
# =========================================================================  
#  
# Copyright © 2017, 2018. EarthWalk Software  
# Licensed under the GNU General Public License, GPL-3.0-or-later.  
#  
# This file is part of ewsdocker/debian-kaptain-menu.  
#  
# ewsdocker/debian-kaptain-menu is free software: you can redistribute  
# it and/or modify it under the terms of the GNU General Public License  
# as published by the Free Software Foundation, either version 3 of the  
# License, or (at your option) any later version.  
#  
# ewsdocker/debian-kaptain-menu is distributed in the hope that it will  
# be useful, but WITHOUT ANY WARRANTY; without even the implied warranty  
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with ewsdocker/debian-kaptain-menu. If not, see  
# <http://www.gnu.org/licenses/>.  
#  
# =========================================================================  
# =========================================================================  
#  
# for sample docker run command,  
# refer to /usr/local/share/kaptain/samples  
#  
# =========================================================================  
# =========================================================================  
FROM ewsdocker/debian-kaptain:1.0.2  
MAINTAINER Jay Wheeler <EarthWalkSoftware@gmail.com>  
  
# =========================================================================  
ENV DEBIAN_FRONTEND=noninteractive \  
KPT_USER=kpt \  
KPT_UID=1000 \  
KPT_HOME="" \  
KPT_MENU="" \  
KPT_DEFMENU="kaptain-sample-docker" \  
KPT_RUNTYPE="run" \  
KPT_TEST=0 \  
KPT_OPTIONS="" \  
LMSOPT_QUIET=0  
# =========================================================================  
ENV PACKAGE_RELEASE="debian-kaptain" \  
PACKAGE_VERS="1.0.2" \  
LMSBUILD_NAME="debian-kaptain-menu" \  
LMSBUILD_VERSION="1.0.3"  
ENV LMSBUILD_DOCKER="ewsdocker/${LMSBUILD_NAME}:${LMSBUILD_VERSION}" \  
LMSBUILD_PACKAGE="${PACKAGE_RELEASE}:${PACKAGE_VERS}"  
# =========================================================================  
COPY scripts/. /  
  
# =========================================================================  
RUN apt-get update -y \  
&& printf "${LMSBUILD_DOCKER} (${LMSBUILD_PACKAGE}), %s @ %s\n" `date
'+%Y-%m-%d'` `date '+%H:%M:%S'` >> /etc/ewsdocker-builds.txt  
  
# =========================================================================  
VOLUME /dest  
VOLUME /hostdev  
  
VOLUME /menu  
VOLUME /userbin  
  
# =========================================================================  
ENTRYPOINT ["/my_init", "--quiet"]  
CMD ["/usr/bin/kaptain-menu"]  

