#########################################################################  
# Container: mat231228/spotify-streamer #  
# Version: 0.0.1 #  
# #  
# Description: #  
# A container to stream Spotify on a LAN #  
# #  
# This program is free software; you can redistribute it and/or modify #  
# it under the terms of the GNU General Public License as published by #  
# the Free Software Foundation; either version 2 of the License, or #  
# (at your option) any later version. #  
# #  
# This program is distributed in the hope that it will be useful, #  
# but WITHOUT ANY WARRANTY; without even the implied warranty of #  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the #  
# GNU General Public License for more details. #  
# #  
# You should have received a copy of the GNU General Public License #  
# along with this program; if not, write to the #  
# Free Software Foundation, Inc., #  
# 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA. #  
# #  
#########################################################################  
  
FROM matl/x11-novnc:latest  
  
MAINTAINER mat231228 <mat231228@users.noreply.github.com>  
  
# Expose Port  
EXPOSE 8081  
  
RUN DEBIAN_FRONTEND=noninteractive apt-key adv --keyserver
hkp://keyserver.ubuntu.com:80 --recv-keys
BBEBDCB318AD50EC6865090613B00F1FD2C19886  
RUN DEBIAN_FRONTEND=noninteractive echo deb http://repository.spotify.com
stable non-free | tee /etc/apt/sources.list.d/spotify.list  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qq  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install spotify-client  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install libpangoxft-1.0-0
libpangox-1.0-0 xauth pulseaudio  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install vlc  
  
ADD start-spotify.sh /usr/bin/start-spotify.sh  
RUN chmod +x /usr/bin/start-spotify.sh  
  
ADD stream-spotify.sh /usr/bin/stream-spotify.sh  
RUN chmod +x /usr/bin/stream-spotify.sh  
  
RUN useradd -d /home/spotify -p "!" -m -g audio -c "Docker-Spotify" spotify  
VOLUME /home/spotify/  
  
COPY spotify.conf /etc/supervisor/conf.d/spotify.conf  
CMD ["/usr/bin/supervisord"]  

