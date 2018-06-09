FROM tarot13/v2ray  
  
LABEL maintainer "Ian Li <OpenSource@ianli.xyz>"  
  
RUN mkdir -p /etc/mo/template && \  
cd / && \  
curl -L -O https://github.com/techotaku/docker-files/raw/master/v2ray-
single/entrypoint.sh && \  
chmod +x entrypoint.sh && \  
cd /etc/mo/template && \  
curl -L -O https://github.com/techotaku/docker-files/raw/master/v2ray-
single/config.json.template  
  
ENTRYPOINT ["/entrypoint.sh"]

