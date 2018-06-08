# meedan/filebeat  
# based on https://github.com/primait/docker-
filebeat/blob/master/1.3/Dockerfile  
FROM meedan/base  
MAINTAINER sysops@meedan.com  
  
ENV FILEBEAT_VERSION=5.0.0-beta1 \  
FILEBEAT_URL=https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-5.0.0-beta1-linux-x86_64.tar.gz
\  
FILEBEAT_SHA1=a2327f38b487525b75e8132ae30a01d64e24c829  
  
RUN set -x && \  
curl -o /opt/filebeat.tar.gz ${FILEBEAT_URL} && \  
cd /opt && \  
echo "${FILEBEAT_SHA1} filebeat.tar.gz" | sha1sum -c - && \  
tar xzvf filebeat.tar.gz && \  
cd filebeat-* && \  
cp filebeat /bin && \  
cd /opt && \  
rm -rf filebeat*  
  
COPY bin/docker-entrypoint.sh /  
RUN chmod 755 /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD [ "filebeat", "-e" ]

