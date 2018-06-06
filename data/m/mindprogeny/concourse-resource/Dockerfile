FROM alpine:edge  
  
RUN apk --no-cache add bash jq tar curl && \  
curl -skL "$(curl -s
https://api.github.com/repos/prometheus/alertmanager/releases/latest|jq --raw-
output '.assets[] | .browser_download_url' | grep 'linux-amd64')" >
/tmp/am.tgz && \  
tar xzf /tmp/am.tgz -C /tmp --wildcards */amtool -O > /usr/local/bin/amtool &&
\  
rm /tmp/am.tgz && \  
chmod +x /usr/local/bin/amtool && \  
apk del tar curl  
  
ADD check /opt/resource/check  
ADD in /opt/resource/in  
ADD out /opt/resource/out  
ADD common.sh /opt/resource/common.sh  
  
RUN chmod +x /opt/resource/*  

