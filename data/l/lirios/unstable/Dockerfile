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
FROM python:3-alpine AS builder  
MAINTAINER Pier Luigi Fiorini <pierluigi.fiorini@liri.io>  
ARG arch=x86_64  
RUN apk add --no-cache tar curl  
RUN pip install requests  
ARG today=1  
RUN curl
https://raw.githubusercontent.com/lirios/archbuild/master/docker/createrootfs/createrootfs.py
> createrootfs.py \  
&& python createrootfs.py --arch=${arch} \--nameserver=8.8.8.8 --siglevel-
never --lirios-repo  
  
FROM scratch  
MAINTAINER Pier Luigi Fiorini <pierluigi.fiorini@liri.io>  
ARG today=1  
ARG arch=x86_64  
COPY \--from=builder root.${arch}/ /  
RUN curl
https://raw.githubusercontent.com/lirios/archbuild/master/docker/createrootfs/setup.sh
> setup.sh \  
&& bash setup.sh && rm -f setup.sh  
COPY build.sh .  
RUN ./build.sh && rm -f build.sh  
ADD startsession /usr/bin/startsession  
ENV XDG_RUNTIME_DIR=/run/lirios  
USER lirios  
WORKDIR /home/lirios  
CMD ["/usr/bin/startsession"]  

