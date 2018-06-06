#  
# Copyright 2017 Cluehub  
#  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
#  
FROM openjdk:8-jre  
  
MAINTAINER cluehub  
  
ARG scala_version=2.11  
ARG kafka_version=0.11.0.1  
ENV DEBIAN_FRONTEND noninteractive  
ENV SCALA_VERSION=$scala_version KAFKA_VERSION=$kafka_version  
ENV KAFKA_FILE_NAME kafka_"$SCALA_VERSION"-"$KAFKA_VERSION"  
ENV KAFKA_KEYRING /tmp/kafka-keyring.gpg  
ENV KAFKA_KEYS /tmp/KAFKA_KEYS  
ENV KAFKA_SIG /tmp/"$KAFKA_FILE_NAME".tgz.asc  
ENV KAFKA_ARCHIVE=/tmp/"$KAFKA_FILE_NAME".tgz  
ENV KAFKA_HOME /opt/"$KAFKA_FILE_NAME"  
ENV KAFKA_SERVER_log_dirs /data  
ENV KAFKA_LOG4J_appender_kafkaAppender_File=/datalog/server.log  
ENV KAFKA_LOG4J_appender_stateChangeAppender_File=/datalog/state-change.log  
ENV KAFKA_LOG4J_appender_requestAppender_File=/datalog/kafka-request.log  
ENV KAFKA_LOG4J_appender_cleanerAppender_File=/datalog/log-cleaner.log  
ENV KAFKA_LOG4J_appender_controllerAppender_File=/datalog/controller.log  
ENV KAFKA_LOG4J_appender_authorizerAppender_File=/datalog/kafka-authorizer.log  
  
VOLUME ["/data"]  
VOLUME ["/datalog"]  
  
COPY 01.download-kafka.sh /tmp/.  
COPY 02.verify-download.sh /tmp/.  
COPY 03.install-kafka.sh /tmp/.  
COPY start-kafka.sh /usr/bin/.  
  
RUN chmod a+x /usr/bin/start-kafka.sh && chmod a+x /tmp/*.sh && for f in `ls
-1 /tmp/*.sh`; do $f; if [ $? -ne 0 ]; then break; fi; done; rm /tmp/*.sh  
  
EXPOSE 9092  
ENTRYPOINT ["start-kafka.sh"]  

