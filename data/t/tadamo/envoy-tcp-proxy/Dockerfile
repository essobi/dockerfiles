FROM envoyproxy/envoy:latest  
RUN apt-get update && \  
apt-get install -y \  
jq && \  
chgrp -R 0 /etc && \  
chmod -R g=u /etc  
COPY envoy.json /etc/envoy-conf.json  
COPY entrypoint.sh /usr/local/bin  
ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]  

