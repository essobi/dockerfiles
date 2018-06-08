#  
# This file is part of Liri.  
#  
# Copyright (C) 2017 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com>  
#  
# $BEGIN_LICENSE:GPL3+$  
#  
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
#  
# This program is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with this program. If not, see <http://www.gnu.org/licenses/>.  
#  
# $END_LICENSE$  
#  
FROM liridev/archlinux-base  
ADD pacman-repo.conf /tmp/pacman-repo.conf  
ADD entrypoint /bin/entrypoint  
ARG CACHEBUST=1  
RUN mkdir -p /build && \  
mkdir -p /repo && \  
mkdir -p /worker && \  
cat /tmp/pacman-repo.conf >> /etc/pacman.conf && \  
rm -f /tmp/pacman-repo.conf && \  
sed -i -e 's,^#MAKEFLAGS=,MAKEFLAGS=,g' /etc/makepkg.conf && \  
pacman -Syu --noconfirm && \  
pacman-db-upgrade && \  
pacman -S --noconfirm git python-pip python-yaml flatpak flatpak-builder && \  
rm -f /var/cache/pacman/pkg/*.pkg.tar.* && \  
pip install buildbot-worker==1.1.1 && \  
useradd -u 1000 -s /bin/bash -m builduser && \  
passwd -d builduser && \  
chown -R builduser /build && \  
chown -R builduser /worker && \  
echo "builduser ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/makepkg  
VOLUME /build  
VOLUME /repo  
USER builduser  
WORKDIR /worker  
CMD ["/bin/entrypoint"]  

