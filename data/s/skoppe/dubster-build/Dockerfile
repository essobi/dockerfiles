# Dubster. Runs unittests on dub packages against latest dmd compiler's  
# Copyright (C) 2016 Sebastiaan Koppe  
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
FROM skoppe/dbuild:v2.071.1-1  
MAINTAINER "Sebastiaan Koppe"  
  
RUN pacman --noconfirm -Sy --force nodejs npm && \  
# Delete any backup files like /etc/pacman.d/gnupg/pubring.gpg~  
find /. -name "*~" -type f -delete && \  
  
# Clean up pacman  
bash -c "echo 'y' | pacman -Scc >/dev/null 2>&1" && \  
paccache -rk0 >/dev/null 2>&1 && \  
pacman-optimize && \  
rm -r /var/lib/pacman/sync/*

