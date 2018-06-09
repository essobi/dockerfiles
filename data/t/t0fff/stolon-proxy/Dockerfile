FROM postgres:9.6.8  
  
ENV STPROXY_CLUSTER_NAME=stolon-cluster \  
STPROXY_STORE_BACKEND=etcdv3 \  
STPROXY_STORE_ENDPOINTS=http://localhost:2379 \  
STPROXY_LISTEN_ADDRESS=0.0.0.0 \  
STPROXY_PORT=25432  
#COPY bin/stolon-proxy bin/stolonctl /usr/local/bin/  
  
RUN apt-get update && apt-get install -y wget && \  
mkdir -p /tmp/stolon-binary && \  
wget -qO-
https://github.com/T0FFF/stolon/releases/download/v0.10.1/stolon-v0.10.1.tar.gz
| tar -xz -C /tmp/stolon-binary && \  
mv /tmp/stolon-binary/* /usr/local/bin/ && \  
apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y && rm -rf
/var/lib/{apt,dpkg,cache,log} && \  
find /tmp /var/tmp /run /var/log -mindepth 1 -delete -print  
  
RUN chmod +x /usr/local/bin/stolon-proxy /usr/local/bin/stolonctl  
  
USER postgres  
ENTRYPOINT ["stolon-proxy"]  

