FROM postgres:9.6.2  
ENV STOLON_VERSION=0.5.0 \  
STOLON_INITIAL_CLUSTER_SPEC=/etc/stolon/init-spec.json \  
STOLON_DATA_DIR=/data/postgres  
  
RUN echo "--- Install build requirements ---" && \  
apt-get update && \  
apt-get install -y curl && \  
echo "--- Install stolon ---" && \  
curl -SL
https://github.com/sorintlab/stolon/releases/download/v${STOLON_VERSION}/stolon-v${STOLON_VERSION}-linux-
amd64.tar.gz | tar -xz && \  
mv stolon-v${STOLON_VERSION}-linux-amd64/stolon-sentinel /usr/bin && \  
mv stolon-v${STOLON_VERSION}-linux-amd64/stolon-proxy /usr/bin && \  
mv stolon-v${STOLON_VERSION}-linux-amd64/stolon-keeper /usr/bin && \  
mv stolon-v${STOLON_VERSION}-linux-amd64/stolonctl /usr/bin && \  
mkdir -p ${STOLON_DATA_DIR} && \  
chmod 700 ${STOLON_DATA_DIR} && \  
chown postgres -R ${STOLON_DATA_DIR} && \  
echo "--- Remove build requirements ---" && \  
rm -rf stolon-v${STOLON_VERSION}-linux-amd64 && \  
apt-get clean  
  
COPY init-spec.json ${STOLON_INITIAL_CLUSTER_SPEC}  
  
VOLUME ["${STOLON_DATA_DIR}"]  
  
USER postgres  

