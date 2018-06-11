FROM alpine:3.6  
LABEL maintainer="Wondershake"  
  
  
# Default Environment Variables  
  
ENV MYSQL_HOST "127.0.0.1"  
ENV MYSQL_PORT "3306"  
ENV MYSQL_USER "root"  
  
ENV BACKUP_TO "s3"  
  
ENV S3_PREFIX ""  
ENV GCS_PREFIX ""  
  
ENV BZIP2_LEVEL "9"  
  
  
# Build Configuration  
  
ENV GCLOUD_SDK_VERSION "170.0.0"  
  
RUN apk update \  
  
# Install Dependencies  
&& apk \--no-cache add \  
bash \  
python2 \  
py-pip \  
mariadb-client \  
  
&& apk \--no-cache add --virtual .build-deps \  
curl \  
  
# AWS CLI  
&& pip \--no-cache-dir install \  
awscli \  
  
# Google Cloud SDK  
&& mkdir /opt \  
&& cd /opt \  
&& curl -o /opt/google-cloud-sdk.tar.gz \  
https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-${GCLOUD_SDK_VERSION}-linux-x86_64.tar.gz \  
&& tar zxf google-cloud-sdk.tar.gz \  
&& rm google-cloud-sdk.tar.gz \  
&& CLOUDSDK_PYTHON=$(which python2) \  
google-cloud-sdk/install.sh \  
\--usage-reporting=false \  
\--rc-path=/etc/profile.d/gcloud.sh \  
\--quiet \  
&& bash -lc "yes | gcloud components update"  
  
COPY entrypoint.sh /opt/entrypoint.sh  
  
CMD sh /opt/entrypoint.sh  

