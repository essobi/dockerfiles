FROM debian:stretch-slim  
LABEL maintainer="ewa@ai-traders.com"  
  
RUN apt-get update &&\  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends\  
curl gnupg2 wget nano ca-certificates &&\  
apt-get -y autoremove && apt-get -y autoclean && apt-get -y clean &&\  
rm -rf /tmp/* /var/tmp/* && rm -rf /var/lib/apt/lists/*  
  
RUN wget --tries=3 --retry-connrefused --wait=3 --random-wait --quiet --show-
progress --progress=bar:force
https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64 &&\  
chmod +x ./jq-linux64 &&\  
mv ./jq-linux64 /usr/bin/jq  
  
# using `curl -sL https://deb.nodesource.com/setup_9.x | bash -`  
# does not show errors, so let's wget it  
RUN wget -O /tmp/node-setup_9.x https://deb.nodesource.com/setup_9.x &&\  
chmod +x /tmp/node-setup_9.x &&\  
/tmp/node-setup_9.x &&\  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends\  
nodejs=9.4.0-1nodesource1 &&\  
apt-get -y autoremove && apt-get -y autoclean && apt-get -y clean &&\  
rm -rf /tmp/* /var/tmp/* && rm -rf /var/lib/apt/lists/*  
  
# Allow using tp-api from any path, for experimenting.  
RUN npm install --global tp-api@1.2.2  
ENV NODE_PATH=/usr/lib/node_modules  
  
COPY ./backup /opt/tp_backup  
COPY version.txt /opt/tp_backup/version.txt  
RUN cd /opt/tp_backup &&\  
chmod +x /opt/tp_backup/*.sh  
  
ENTRYPOINT ["/bin/bash", "-c"]  
CMD ["/opt/tp_backup/run.sh"]  

