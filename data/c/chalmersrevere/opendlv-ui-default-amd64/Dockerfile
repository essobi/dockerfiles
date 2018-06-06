# Copyright (C) 2018 Ola Benderius  
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
FROM chalmersrevere/opendlv-ui-server-amd64:v0.0.8  
MAINTAINER Ola Benderius "ola.benderius@chalmers.se"  
COPY ./http/ /srv/http  
ENTRYPOINT ["/usr/bin/opendlv-ui-server", "--http-root=/srv/http", "--
port=8000"]  

