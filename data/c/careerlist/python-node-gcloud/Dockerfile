FROM careerlist/python-app:3.6-slim  
  
LABEL maintainer="careerlist"  
  
ENV NODE_VERSION 8.9.4  
RUN apt-get update && apt-get install -y --no-install-recommends \  
xz-utils \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 --no-same-owner \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" \  
&& apt-get purge -y --auto-remove \  
xz-utils \  
&& rm -rf /var/lib/apt/lists/* \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
ENV GOOGLE_DIR=/google \  
GCLOUD_BINARY_VERSION=200.0.0 \  
ADDITIONAL_COMPONENTS=beta  
  
WORKDIR ${GOOGLE_DIR}  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
python \  
&& curl -SLO
"https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-${GCLOUD_BINARY_VERSION}-linux-x86_64.tar.gz" \  
&& tar -xzf "google-cloud-sdk-${GCLOUD_BINARY_VERSION}-linux-x86_64.tar.gz" \  
&& rm "google-cloud-sdk-${GCLOUD_BINARY_VERSION}-linux-x86_64.tar.gz" \  
&& google-cloud-sdk/install.sh --usage-reporting=false \--path-update=false
\--bash-completion=false \--additional-components $ADDITIONAL_COMPONENTS \  
&& google-cloud-sdk/bin/gcloud config set \--installation
component_manager/disable_update_check true \  
&& rm -rf google-cloud-sdk/.install/.backup \  
&& rm -rf google-cloud-sdk/.install/.download \  
&& curl -SLo cloud_sql_proxy -nv
"https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64" \  
&& chmod +x cloud_sql_proxy \  
&& mkdir /cloudsql \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV CLOUDSDK_PYTHON=/usr/bin/python2.7 \  
PATH=${PATH}:${GOOGLE_DIR}:${GOOGLE_DIR}/google-cloud-sdk/bin  
  
WORKDIR ${APP_DIR}  

