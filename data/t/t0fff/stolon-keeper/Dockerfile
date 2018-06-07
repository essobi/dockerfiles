FROM postgres:9.6.8  
ENV STKEEPER_CLUSTER_NAME=stolon-cluster \  
STKEEPER_STORE_BACKEND=etcdv3 \  
STKEEPER_STORE_ENDPOINTS=http://localhost:2379 \  
STKEEPER_DATA_DIR=/data/postgres  
  
RUN mkdir -p ${STKEEPER_DATA_DIR} && \  
chmod 700 ${STKEEPER_DATA_DIR} && \  
chown postgres -R ${STKEEPER_DATA_DIR}  
VOLUME ["${STKEEPER_DATA_DIR}"]  
  
COPY etc/keeper-entrypoint.sh /usr/local/bin/  
#COPY bin/stolon-keeper bin/stolonctl /usr/local/bin/  
RUN apt-get update && apt-get install -y wget && \  
mkdir -p /tmp/stolon-binary && \  
wget -qO-
https://github.com/T0FFF/stolon/releases/download/v0.10.1/stolon-v0.10.1.tar.gz
| tar -xz -C /tmp/stolon-binary && \  
mv /tmp/stolon-binary/* /usr/local/bin/ && \  
apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y && rm -rf
/var/lib/{apt,dpkg,cache,log} && \  
find /tmp /var/tmp /run /var/log -mindepth 1 -delete -print  
  
USER postgres  
ENTRYPOINT ["keeper-entrypoint.sh"]  

