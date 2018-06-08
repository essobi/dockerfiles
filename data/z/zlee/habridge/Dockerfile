# habridge for Dockerfile  
FROM nimmis/alpine-java  
MAINTAINER ilee  
  
ENV habridge_version=5.2.1 \  
habridge_DIR=/usr/local/habridge  
  
RUN set -ex && \  
habridge_latest=https://github.com/bwssytems/ha-
bridge/releases/download/v${habridge_version}/ha-
bridge-${habridge_version}.jar && \  
habridge_latest_filename=ha-bridge-${habridge_version}.jar && \  
sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories
&& \  
apk update && \  
apk upgrade && \  
apk add --no-cache wget bash && \  
[ ! -d ${habridge_DIR} ] && mkdir -p ${habridge_DIR} && cd ${habridge_DIR} &&
\  
wget --no-check-certificate -q ${habridge_latest} -O
${habridge_latest_filename} && \  
mv ${habridge_DIR}/ha-bridge-${habridge_version}.jar
${habridge_DIR}/habridge.jar && \  
rm -rf /var/cache/apk/* ~/.cache ${habridge_DIR}/${habridge_latest_filename}
${habridge_DIR}/ha-bridge-${habridge_version}.jar  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod u+x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

