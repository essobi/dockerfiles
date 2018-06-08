# polyglot-service: A micro service for natural language processing powered by
Polyglot.  
# Copyright (C) 2017 Turbulent Media inc.  
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
# Victor Yap <vyap@turbulent.ca>  
# c/o Turbulent Media inc.  
# 3981 Saint-Laurent Boulevard  
# Office 888, Montreal (Quebec) Canada  
# H2W 1Y5  
FROM turbulent/polyglot-base  
EXPOSE 80  
RUN mkdir /usr/src/app \  
&& pip install --no-cache-dir bottle  
WORKDIR /usr/src/app  
COPY service.py /usr/src/app/  
CMD python /usr/src/app/service.py  

