FROM node:8.7.0  
#  
# ============================================================================  
#  
# Kyptrack helps you manage your personal budget  
# Copyright (C) 2018 Fanilo Randriamamisoa <fanilo@gmail.com>  
#  
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU Affero General Public License as published  
# by the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
#  
# This program is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU Affero General Public License for more details.  
#  
# You should have received a copy of the GNU Affero General Public License  
# along with this program. If not, see <http://www.gnu.org/licenses/>.  
#  
# ============================================================================  
#  
MAINTAINER Fanilo Randriamamisoa "fanilo@gmail.com"  
# Create a directory where our app will be placed  
RUN mkdir -p /usr/src/app  
  
# Change directory so that our commands run inside this new directory  
WORKDIR /usr/src/app  
  
# Get all the code needed to run the app  
COPY package.json .  
COPY dist dist  
  
EXPOSE 4000  
COPY entrypoint.sh .  
RUN chmod +x entrypoint.sh  
ENTRYPOINT ["./entrypoint.sh"]  
CMD ["npm", "run", "serve:ssr"]  

