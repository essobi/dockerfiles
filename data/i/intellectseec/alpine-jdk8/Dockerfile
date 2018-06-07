FROM openjdk:8-jre-alpine  
  
EXPOSE 8080  
  
###LOG Configuration#####################################  
RUN mkdir /Intellect-Logs  
ENV INTELLECT_LOG_LOC /Intellect-Logs  
ENV INTELLECT_LOG_FILENAME log-file-name-here-without-extension  
##########################################################  
  
  
###########Docker Cloud Specific Settings ################  
  
###SUPERVISOR  
RUN apk --update add supervisor  
#ADD ./supervisord.conf /etc/supervisord.conf  
####FILEBEAT  
  
ENV FILEBEAT_VERSION 5.6.3  
ENV FILEBEAT_URL
https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-${FILEBEAT_VERSION}-linux-x86_64.tar.gz  
  
WORKDIR /Filebeat  
  
RUN set -ex \  
&& apk add --no-cache --virtual .build-dependencies curl \  
&& curl -fsSL ${FILEBEAT_URL} -o /Filebeat/filebeat.tar.gz \  
&& tar -xzf ./filebeat.tar.gz --strip 1 \  
&& rm -f filebeat.tar.gz \  
&& apk del .build-dependencies  
##########################################################  
  
WORKDIR /opt  
  
ENTRYPOINT ["supervisord", "--nodaemon", "--configuration",
"/etc/supervisord.conf"]  
  

