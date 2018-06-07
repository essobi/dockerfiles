# This file is part of cloud9.  
#  
# cloud9 is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
#  
# cloud9 is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with cloud9 . If not, see <http://www.gnu.org/licenses/>.  
FROM fedora:26  
COPY root /opt/docker/  
RUN ["sh", "/opt/docker/run.root.sh"]  
USER user  
RUN ["sh", "/opt/docker/run.user.sh"]  
ENTRYPOINT ["sh", "/opt/docker/entrypoint.sh"]  
CMD []

