FROM postgres:9.6.8  
ENV STSENTINEL_CLUSTER_NAME=stolon-cluster \  
STSENTINEL_STORE_BACKEND=etcdv3 \  
STSENTINEL_STORE_ENDPOINTS=http://localhost:2379 \  
STSENTINEL_INITIAL_CLUSTER_SPEC=/etc/stolon/init-spec.json  
  
#COPY bin/stolon-sentinel bin/stolonctl /usr/local/bin/  
COPY etc/init-spec.json ${STSENTINEL_INITIAL_CLUSTER_SPEC}  
  
RUN apt-get update && apt-get install -y wget && \  
mkdir -p /tmp/stolon-binary && \  
wget -qO- https://github.com/orange-
cloudfoundry/stolon/releases/download/v0.10.1/stolon-v0.10.1.tar.gz | tar -xz
-C /tmp/stolon-binary && \  
mv /tmp/stolon-binary/* /usr/local/bin/ && \  
apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y && rm -rf
/var/lib/{apt,dpkg,cache,log} && \  
find /tmp /var/tmp /run /var/log -mindepth 1 -delete -print  
  
RUN chmod +x /usr/local/bin/stolon-sentinel /usr/local/bin/stolonctl  
  
USER postgres  
ENTRYPOINT ["stolon-sentinel"]  

