#
==============================================================================  
# mykro/jetbrains-youtrack - A build on top of Debian 8 (Jessie)  
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
# docker pull mykro/jetbrains-youtrack:[latest|6.5.17015|6.5.16981]  
#  
# Build with:  
# docker pull mykro/java8-jre:latest  
# docker build -t some-repo/some-youtrack mykro/jetbrains-youtrack .  
#  
# Run with:  
# docker run -d \  
# -p 10401:8080 \  
# -v /jetbrains/youtrack/:/jetbrains/youtrack/ \  
# -v /jetbrains/youtrack/backup:/jetbrains/youtrack/backup \  
# -v /jetbrains/youtrack/data:/jetbrains/youtrack/data \  
# -v /jetbrains/youtrack/logs:/jetbrains/youtrack/logs \  
# -v /jetbrains/youtrack/tmp:/jetbrains/youtrack/tmp \  
# --name=jetbrains-youtrack-001 \  
# --restart=always \  
# mykro/jetbrains-youtrack  
#
==============================================================================  
FROM mykro/java8-jre:latest  
MAINTAINER Matthew Hartstonge <matt@mykro.co.nz>  
  
#
==============================================================================  
# -------------------------------- Edit Me
-------------------------------------  
ENV YOUTRACK_MAJOR 6.5  
ENV YOUTRACK_MINOR 17015  
# Create a non-root user  
ENV YOUTRACK_USER docker  
  
# Java and Jetty Configuration  
# Sidenote: Port 80/443 requires a sudoer  
ENV YOUTRACK_RAM 1024m  
ENV YOUTRACK_URL "http://localhost"  
ENV YOUTRACK_PORT 8080  
# Exposed Host Volumes  
ENV YOUTRACK_HOME "/jetbrains/youtrack"  
ENV YOUTRACK_BACKUP_DIR "${YOUTRACK_HOME}/backup"  
ENV YOUTRACK_DATA_DIR "${YOUTRACK_HOME}/data"  
ENV YOUTRACK_LOG_DIR "${YOUTRACK_HOME}/logs"  
ENV YOUTRACK_TEMP_DIR "${YOUTRACK_HOME}/tmp"  
# Web Application Directory  
ENV WEBAPP_DIR "/webapps/jetbrains"  
# -------------------------------- Edit Me
-------------------------------------  
#
==============================================================================  
RUN mkdir -p ${YOUTRACK_BACKUP_DIR} \  
&& mkdir -p ${YOUTRACK_DATA_DIR} \  
&& mkdir -p ${YOUTRACK_LOG_DIR} \  
&& mkdir -p ${YOUTRACK_TEMP_DIR} \  
&& mkdir -p ${WEBAPP_DIR}/youtrack \  
&& groupadd -r ${YOUTRACK_USER} \  
&& useradd -r -g ${YOUTRACK_USER} -d ${YOUTRACK_HOME} ${YOUTRACK_USER} \  
&& apt-get update && apt-get install -y unzip \  
&& wget
https://download.jetbrains.com/charisma/youtrack-${YOUTRACK_MAJOR}.${YOUTRACK_MINOR}.zip
\  
&& unzip youtrack-${YOUTRACK_MAJOR}.${YOUTRACK_MINOR}.zip -d
${WEBAPP_DIR}/youtrack \  
&& rm youtrack-${YOUTRACK_MAJOR}.${YOUTRACK_MINOR}.zip \  
&& rm -rf ${WEBAPP_DIR}/youtrack/internal/java \  
&& ${WEBAPP_DIR}/youtrack/bin/youtrack.sh configure \  
\--backups-dir ${YOUTRACK_BACKUP_DIR} \  
\--data-dir ${YOUTRACK_DATA_DIR} \  
\--logs-dir ${YOUTRACK_LOG_DIR} \  
\--temp-dir ${YOUTRACK_TEMP_DIR} \  
\--listen-port ${YOUTRACK_PORT} \  
\--base-url ${YOUTRACK_URL} \  
&& ${WEBAPP_DIR}/youtrack/bin/youtrack.sh configure -J-Xmx${YOUTRACK_RAM} \  
&& chown -Rv ${YOUTRACK_USER}:${YOUTRACK_USER} ${WEBAPP_DIR} \  
&& chown -R ${YOUTRACK_USER}:${YOUTRACK_USER} ${YOUTRACK_HOME} \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
USER ${YOUTRACK_USER}  
WORKDIR ${WEBAPP_DIR}/youtrack  
ENTRYPOINT ["bin/youtrack.sh"]  
CMD ["run"]  
EXPOSE ${YOUTRACK_PORT}  
VOLUME ["${YOUTRACK_BACKUP_DIR}", "${YOUTRACK_DATA_DIR}",
"${YOUTRACK_LOG_DIR}", "${YOUTRACK_TEMP_DIR}"]  

