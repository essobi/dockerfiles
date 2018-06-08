FROM golang:1.6.3-alpine  
MAINTAINER David Papp <david@ghostmonitor.com>  
  
  
#COPY ./traefik_linux-amd64 /usr/local/bin/traefik  
  
RUN apk --update add \  
curl \  
jq \  
bash \  
wget \  
ca-certificates && \  
update-ca-certificates && \  
curl -s https://api.github.com/repos/containous/traefik/releases/latest | jq
.assets[].browser_download_url | grep -E linux-amd64 | xargs wget -qO- -O
/usr/local/bin/traefik && \  
chmod +x /usr/local/bin/traefik && \  
rm -f /var/cache/apk/* && \  
mkdir -p /var/log/traefik/access && \  
mkfifo /var/log/traefik/access/pipe && \  
chmod a+rwx /var/log/traefik/access/pipe  
  
  
  
# WORKDIR /usr/src  
# ADD ./etc/rsyslog.conf /etc/rsyslog.conf  
# ADD ./etc/rsyslog.d/50-default.conf /etc/rsyslog.d/50-default.conf  
# ADD start.sh /usr/src/  
# ADD syslog.sh /usr/src/  
  
  
# ENTRYPOINT ["./syslog.sh"]  
CMD ["traefik"]  

