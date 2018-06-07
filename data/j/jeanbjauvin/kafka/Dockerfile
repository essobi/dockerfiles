# Builds an image for Apache Kafka 0.10.2.1  
# This file is part of kafka-docker.  
#  
# kafka-docker is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, either version 3 of the License, or  
# (at your option) any later version.  
#  
# kafka-docker is distributed in the hope that it will be useful,  
# but WITHOUT ANY WARRANTY; without even the implied warranty of  
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the  
# GNU General Public License for more details.  
#  
# You should have received a copy of the GNU General Public License  
# along with kafka-docker. If not, see <http://www.gnu.org/licenses/>.  
# The openjdk:8-alpine base image runs OpenJDK 8 installed atop the  
# alpine:3.5 official image. Docker's official Java images are  
# OpenJDK-only currently and the Kafka project recommend using  
# Oracle Java for production for optimal performance.  
# This image is therefore mostly for open-source projects.  
FROM openjdk:8-alpine  
  
LABEL maintainer="Jean Bruno JAUVIN <jeanbjauvin@gmail.com>" \  
name="Kafka" \  
version="0.11.0.1"  
  
ENV KAFKA_VERSION=0.11.0.1 \  
KAFKA_SCALA_VERSION=2.12 \  
KAFKA_HOME=/kafka \  
JMX_PORT=7203  
RUN mkdir /kafka /data /logs \  
&& apk add --no-cache wget bash \  
&& wget -q -O -
http://www.us.apache.org/dist/kafka/${KAFKA_VERSION}/kafka_${KAFKA_SCALA_VERSION}-${KAFKA_VERSION}.tgz
| tar -xzf - -C /tmp \  
&& mv /tmp/kafka_*/* ${KAFKA_HOME} \  
&& rm -rf /tmp/kafka_* \  
&& addgroup -S kafka \  
&& adduser -h /kafka -G kafka -S -H -s /sbin/nologin kafka \  
&& chown -R kafka:kafka /kafka /data /logs  
  
COPY config /kafka/config  
COPY start.sh /start.sh  
RUN chmod +x /start.sh  
  
USER kafka  
  
EXPOSE 9092 ${JMX_PORT}  
VOLUME [ "/data", "/logs" ]  
  
ENTRYPOINT [ "/start.sh" ]  

