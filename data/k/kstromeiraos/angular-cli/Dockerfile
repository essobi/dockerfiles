# Angular CLI (latest) on Node 6.10.0  
# Copyright (C) 2017 José Antonio López <dev@kstromeiraos.com>  
#  
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
# This program is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
# You should have received a copy of the GNU General Public License  
# along with this program. If not, see <http://www.gnu.org/licenses/>.  
FROM node:6.10.0  
MAINTAINER José Antonio López <dev@kstromeiraos.com>  
  
RUN useradd --user-group --create-home --shell /bin/false app  
  
ENV HOME=/home/app  
WORKDIR $HOME  
  
RUN npm install -g @angular/cli && npm cache clean  
  
# 4200 = Webpack port  
# 49153 = Live reload port  
EXPOSE 4200 49153  
ENTRYPOINT ["/bin/bash", "-c"]  

