FROM consul:1.0.3  
MAINTAINER Tim Hartmann <tim.hartmann@runkeeper.com> (@paxindustria)  
  
RUN \  
apk update && \  
apk -Uuv add groff less python py-pip jq bind-tools && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm /var/cache/apk/*  
  
COPY scripts/instance-status.sh /usr/local/bin/instance-status.sh  
COPY scripts/instance-status-handler.sh /usr/local/bin/instance-status-
handler.sh  
COPY services/consul_backup.json /consul/config/consul_backup.json  
COPY scripts/consul-backup.sh /usr/local/bin/consul-backup.sh  

