#
==============================================================================  
# mykro/jetbrains-upsource - A build on top of Debian 8 (Jessie)  
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
# docker pull mykro/jetbrains-upsource:[latest|2.5.5047]  
#  
# Build with:  
# docker pull mykro/java8-jre:latest  
# docker build -t some-repo/some-upsource mykro/jetbrains-upsource .  
#  
# Run with:  
# docker run -d \  
# -p 10301:8080 \  
# -v /jetbrains/upsource/:/jetbrains/upsource/ \  
# -v /jetbrains/upsource/backup:/jetbrains/upsource/backup \  
# -v /jetbrains/upsource/data:/jetbrains/upsource/data \  
# -v /jetbrains/upsource/logs:/jetbrains/upsource/logs \  
# -v /jetbrains/upsource/tmp:/jetbrains/upsource/tmp \  
# --name=jb-us-001 \  
# --restart=always \  
# mykro/jetbrains-upsource  
#  
# Pull image with:  
# docker pull mykro/jetbrains-upsource:[latest|2.5.5047|2.5.4995]  
#  
# Build with:  
# docker pull mykro/java8-jre:latest  
# docker build -t some-repo/some-upsource mykro/jetbrains-upsource .  
#
==============================================================================  
FROM mykro/java8-jre:latest  
MAINTAINER Matt Hartstonge <matt@mykro.co.nz>  
  
#
==============================================================================  
# -------------------------------- Edit Me
-------------------------------------  
# Download the latest version  
ENV UPSOURCE_MAJOR 2.5  
ENV UPSOURCE_MINOR 5047  
# Create a non-root user  
ENV UPSOURCE_USER docker  
  
# Java and Jetty Configuration  
# Sidenote: Port 80/443 requires a sudoer  
ENV UPSOURCE_RAM 1024m  
ENV UPSOURCE_URL "http://localhost"  
ENV UPSOURCE_PORT 8080  
# Exposed Host Volumes  
ENV UPSOURCE_HOME "/jetbrains/upsource"  
ENV UPSOURCE_BACKUP_DIR "${UPSOURCE_HOME}/backup"  
ENV UPSOURCE_DATA_DIR "${UPSOURCE_HOME}/data"  
ENV UPSOURCE_LOG_DIR "${UPSOURCE_HOME}/logs"  
ENV UPSOURCE_TEMP_DIR "${UPSOURCE_HOME}/tmp"  
# Web Application Directory  
ENV WEBAPP_DIR "/webapps/jetbrains"  
# -------------------------------- Edit Me
-------------------------------------  
#
==============================================================================  
RUN mkdir -p ${UPSOURCE_BACKUP_DIR} \  
&& mkdir -p ${UPSOURCE_DATA_DIR} \  
&& mkdir -p ${UPSOURCE_LOG_DIR} \  
&& mkdir -p ${UPSOURCE_TEMP_DIR} \  
&& mkdir -p ${WEBAPP_DIR} \  
&& groupadd -r ${UPSOURCE_USER} \  
&& useradd -r -g ${UPSOURCE_USER} -d ${UPSOURCE_HOME} ${UPSOURCE_USER} \  
&& apt-get update && apt-get install -y unzip \  
&& wget
https://download.jetbrains.com/upsource/upsource-${UPSOURCE_MAJOR}.${UPSOURCE_MINOR}.zip
\  
&& unzip upsource-${UPSOURCE_MAJOR}.${UPSOURCE_MINOR}.zip -d ${WEBAPP_DIR} \  
&& rm -fv upsource-${UPSOURCE_MAJOR}.${UPSOURCE_MINOR}.zip \  
&& mv ${WEBAPP_DIR}/Upsource ${WEBAPP_DIR}/upsource \  
&& rm -rfv ${WEBAPP_DIR}/upsource/internal/java \  
&& ${WEBAPP_DIR}/upsource/bin/upsource.sh configure \  
\--backups-dir ${UPSOURCE_BACKUP_DIR} \  
\--data-dir ${UPSOURCE_DATA_DIR} \  
\--logs-dir ${UPSOURCE_LOG_DIR} \  
\--temp-dir ${UPSOURCE_TEMP_DIR} \  
\--listen-port ${UPSOURCE_PORT} \  
\--base-url ${UPSOURCE_URL} \  
&& ${WEBAPP_DIR}/upsource/bin/upsource.sh configure -J-Xmx${UPSOURCE_RAM} \  
&& chown -Rv ${UPSOURCE_USER}:${UPSOURCE_USER} ${WEBAPP_DIR} \  
&& chown -R ${UPSOURCE_USER}:${UPSOURCE_USER} ${UPSOURCE_HOME} \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
USER ${UPSOURCE_USER}  
WORKDIR ${WEBAPP_DIR}/upsource  
ENTRYPOINT ["bin/upsource.sh"]  
CMD ["run"]  
EXPOSE ${UPSOURCE_PORT}  
VOLUME ["${UPSOURCE_BACKUP_DIR}", "${UPSOURCE_DATA_DIR}",
"${UPSOURCE_LOG_DIR}", "${UPSOURCE_TEMP_DIR}"]  

