# Django and Django REST Framework (latest) on Python 3  
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
FROM python:3-alpine  
  
MAINTAINER José Antonio López <dev@kstromeiraos.com>  
  
RUN apk add --update && \  
pip install django && \  
pip install djangorestframework && \  
pip install markdown # Markdown support for the browsable API. \  
&& rm -rf /var/cache/apk/*  
  
RUN mkdir /app  
  
WORKDIR /app  
  
EXPOSE 80  
COPY docker-entrypoint.sh /  
  
RUN chmod 755 /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

