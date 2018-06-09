# Copyright © (C) 2017 Emory Merryman <emory.merryman@gmail.com>  
# This file is part of pass.  
#  
# pass is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
#  
# pass is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with pass. If not, see <http://www.gnu.org/licenses/>.  
FROM emorymerryman/base:0.2.3  
MAINTAINER Emory Merryman emory.merryman@gmail.com  
RUN \  
apk update && \  
apk upgrade && \  
apk add git make bash && \  
WORK_DIR=$(mktemp -d) && \  
git -C ${WORK_DIR} init && \  
git -C ${WORK_DIR} remote add origin https://git.zx2c4.com/password-store && \  
git -C ${WORK_DIR} fetch origin && \  
git -C ${WORK_DIR} checkout tags/1.6.5 && \  
make --directory ${WORK_DIR} install && \  
rm -rf ${WORK_DIR} && \  
apk del git make  
ENTRYPOINT ["/usr/bin/pass"]  
CMD []  

