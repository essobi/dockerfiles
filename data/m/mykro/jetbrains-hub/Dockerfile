#
==============================================================================  
# mykro/jetbrains-hub - A build on top of Debian 8 (Jessie)  
#
------------------------------------------------------------------------------  
# Copyright (C) 2015 Matt Hartstonge  
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
# Java is provided by Oracle and as such, by using of this container, you  
# agree to Oracle's JRE License.  
# Jetbrains Hub is provided by Jetbrains and as such, by using of this  
# container, you agree to Jetbrain's Hub License.  
#  
# Pull image with:  
# docker pull mykro/jetbrains-hub:latest  
#  
# Build with:  
# docker build -t some-repo/some-hub mykro/jetbrains-hub .  
#  
# Run with:  
# docker run -d -p 80:8080 mykro/jetbrains-hub  
#
==============================================================================  
FROM mykro/java8-jre:latest  
MAINTAINER Matt Hartstonge <matt@mykro.co.nz>  
  
#
==============================================================================  
# -------------------------------- Edit Me
-------------------------------------  
# Download the latest version  
# https://download.jetbrains.com/hub/1.0/hub-ring-bundle-1.0.749.zip  
ENV HUB_MAJOR 1.0  
ENV HUB_MINOR 770  
# Create a non-root user  
ENV HUB_USER docker  
  
# Jetty URL and port (remember that port 80 requires a sudoer)  
ENV HUB_URL "http://localhost"  
ENV HUB_PORT 8080  
# Exposed Host Volumes  
ENV HUB_HOME "/jetbrains/hub"  
ENV HUB_BACKUP_DIR "${HUB_HOME}/backup"  
ENV HUB_DATA_DIR "${HUB_HOME}/data"  
ENV HUB_LOG_DIR "${HUB_HOME}/logs"  
ENV HUB_TEMP_DIR "${HUB_HOME}/tmp"  
# Web Application Directory  
ENV WEBAPP_DIR "/webapps/jetbrains"  
# -------------------------------- Edit Me
-------------------------------------  
#
==============================================================================  
RUN mkdir -p ${HUB_BACKUP_DIR} \  
&& mkdir -p ${HUB_DATA_DIR} \  
&& mkdir -p ${HUB_LOG_DIR} \  
&& mkdir -p ${HUB_TEMP_DIR} \  
&& mkdir -p ${WEBAPP_DIR}/hub \  
&& groupadd -r ${HUB_USER} \  
&& useradd -r -g ${HUB_USER} -d ${HUB_HOME} ${HUB_USER} \  
&& apt-get update && apt-get install -y unzip \  
&& wget https://download.jetbrains.com/hub/${HUB_MAJOR}/hub-ring-
bundle-${HUB_MAJOR}.${HUB_MINOR}.zip \  
&& unzip hub-ring-bundle-${HUB_MAJOR}.${HUB_MINOR}.zip -d ${WEBAPP_DIR}/hub \  
&& rm hub-ring-bundle-${HUB_MAJOR}.${HUB_MINOR}.zip \  
&& rm -rf ${WEBAPP_DIR}/hub/internal/java \  
&& ${WEBAPP_DIR}/hub/bin/hub.sh configure \  
\--backups-dir ${HUB_BACKUP_DIR} \  
\--data-dir ${HUB_DATA_DIR} \  
\--logs-dir ${HUB_LOG_DIR} \  
\--temp-dir ${HUB_TEMP_DIR} \  
\--listen-port ${HUB_PORT} \  
\--base-url ${HUB_URL} \  
&& chown -Rv ${HUB_USER}:${HUB_USER} ${WEBAPP_DIR} \  
&& chown -R ${HUB_USER}:${HUB_USER} ${HUB_HOME} \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
USER ${HUB_USER}  
WORKDIR ${WEBAPP_DIR}/hub  
ENTRYPOINT ["bin/hub.sh"]  
CMD ["run"]  
EXPOSE ${HUB_PORT}  
VOLUME ["${HUB_BACKUP_DIR}", "${HUB_DATA_DIR}", "${HUB_LOG_DIR}",
"${HUB_TEMP_DIR}"]  

