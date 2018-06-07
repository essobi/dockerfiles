FROM alpine:3.5  
ENV ENTRYKIT_VER=0.4.0 \  
HYDRA_VER=0.7.7  
RUN apk add --no-cache ca-certificates \  
&& apk add --no-cache --virtual=.build-dependencies curl \  
&& curl -sSL
https://github.com/progrium/entrykit/releases/download/v${ENTRYKIT_VER}/entrykit_${ENTRYKIT_VER}_Linux_x86_64.tgz
\  
| tar -xzC /usr/local/bin \  
&& /usr/local/bin/entrykit --symlink \  
&& mkdir -p /opt/hydra && cd /opt/hydra \  
&& curl -o hydra -L
https://github.com/ory/hydra/releases/download/v${HYDRA_VER}/hydra-linux-amd64
\  
&& chmod +x ./hydra  
# && addgroup hydra -S \  
# && adduser hydra -S -G hydra \  
# && chown root:hydra -R /opt/hydra \  
# && mkdir -p /etc/hydra /var/log/hydra /var/hydra/data \  
# && chown root:hydra -R /etc/hydra \  
# && chown hydra: -R /var/hydra/data /var/log/hydra \  
# && chmod o-rw -R /etc/hydra /var/hydra/data /var/log/hydra  
EXPOSE 4444  
WORKDIR /opt/hydra  
  
ENTRYPOINT /opt/hydra/hydra host  

