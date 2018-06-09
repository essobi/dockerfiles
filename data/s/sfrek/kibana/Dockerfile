FROM debian:stable  
  
ENV KIBANA_VERSION 4.5.4  
  
RUN \  
apt-get update && \  
apt-get install \  
\--assume-yes \  
\--no-install-recommends \  
ca-certificates \  
curl \  
ssl-cert && \  
curl -s \  
-o /tmp/kibana_${KIBANA_VERSION}_amd64.deb \  
https://download.elastic.co/kibana/kibana/kibana_${KIBANA_VERSION}_amd64.deb
&& \  
dpkg -i /tmp/kibana_${KIBANA_VERSION}_amd64.deb && \  
rm /tmp/kibana_${KIBANA_VERSION}_amd64.deb && \  
apt-get remove --purge -fyq \  
curl && \  
apt-get clean -yq && \  
apt-get purge -yq && \  
apt-get autoremove -yq && \  
rm -rf /var/cache/apt/* && \  
rm -rf /var/lib/apt/lists/*  
  
ADD ./run.sh /run.sh  
  
EXPOSE 5601  
  
ENTRYPOINT /run.sh  

