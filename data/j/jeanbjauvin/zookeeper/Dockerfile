# Builds an image for Apache ZooKeeper 3.4.10  
# This file is part of zookeeper-docker.  
#  
# zookeeper-docker is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
#  
# zookeeper-docker is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with zookeeper-docker. If not, see <http://www.gnu.org/licenses/>.  
FROM openjdk:8-alpine  
  
LABEL maintainer="Jean Bruno JAUVIN <jeanbjauvin@gmail.com>" \  
name="ZooKeeper" \  
version="3.4.10"  
  
ENV ZOOKEEPER_VERSION=3.4.10 \  
ZOOKEEPER_HOME=/zookeeper \  
ZOOKEEPER_DATADIR=/data \  
ZOOKEEPER_CONF_DIR=/zookeeper/conf \  
ZOOKEEPER_CLIENT_PORT=2181  
COPY start.sh /start.sh  
  
RUN apk add --no-cache wget bash \  
&& mkdir ${ZOOKEEPER_HOME} ${ZOOKEEPER_DATADIR} \  
&& wget -q -O -
http://www.us.apache.org/dist/zookeeper/zookeeper-${ZOOKEEPER_VERSION}/zookeeper-${ZOOKEEPER_VERSION}.tar.gz
| tar -xzf - -C /tmp \  
&& mv /tmp/zookeeper-*/* ${ZOOKEEPER_HOME} \  
&& rm -rf /tmp/zookeeper-* \  
&& chmod +x /start.sh  
  
COPY zoo.cfg.template ${ZOOKEEPER_CONF_DIR}  
  
EXPOSE 2181 2888 3888  
VOLUME [ "${ZOOKEEPER_CONF_DIR}", "${ZOOKEEPER_DATADIR}" ]  
  
ENTRYPOINT [ "/start.sh" ]  

