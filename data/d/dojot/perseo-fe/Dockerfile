#  
# Copyright 2016 Telefonica Investigación y Desarrollo, S.A.U  
#  
# This file is part of perseo-fe  
#  
# perseo-fe is free software: you can redistribute it and/or modify it under
the terms of the GNU Affero  
# General Public License as published by the Free Software Foundation, either
version 3 of the License, or (at your  
# option) any later version.  
# perseo-fe is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the  
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
the GNU Affero General Public License  
# for more details.  
#  
# You should have received a copy of the GNU Affero General Public License
along with perseo-fe. If not, see  
# http://www.gnu.org/licenses/.  
#  
# For those usages not covered by the GNU Affero General Public License please
contact with iot_support at tid dot es  
#  
FROM node:4  
WORKDIR /opt/perseo-fe  
ENV PERSEO_MONGO_HOST=mongodb  
ENV PERSEO_MONGO_REPLICA_SET=""  
ENV PERSEO_CORE_URL=http://corehost:8080  
EXPOSE 9090  
COPY package.json /opt/perseo-fe/package.json  
COPY npm-shrinkwrap.json /opt/perseo-fe/npm-shrinkwrap.json  
RUN npm install --production  
  
COPY . /opt/perseo-fe/  
CMD bin/perseo  

