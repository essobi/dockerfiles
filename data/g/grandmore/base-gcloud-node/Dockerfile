# based on bigtruedata/gcloud-node  
FROM launcher.gcr.io/google/nodejs  
MAINTAINER Stuart Fenton <stuart@grandmore.com>  
  
# Install node.js 6.11.5  
RUN install_node v6.11.5  
  
# Copy application code.  
COPY . /app/  
  
# Install dependencies.  
RUN npm --unsafe-perm install  
  
# https://cloud.google.com/sdk/docs/#linux  
ENV GCLOUD_DOWNLOAD_URL
https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-187.0.0-linux-x86_64.tar.gz  
ENV GCLOUD_COMPONENTS "beta cloud-datastore-emulator"  
ENV DEBIAN-FRONTEND noninteractive  
RUN apt-get update  
  
# Required Node.js dependencies  
RUN npm install -g \  
apidoc \  
mocha \  
semistandard  
  
# Google Cloud SDK installation  
RUN apt-get install --yes --no-install-recommends \  
openjdk-7-jre  
  
RUN curl ${GCLOUD_DOWNLOAD_URL} > /tmp/gcloud.tar.gz  
RUN tar xzf /tmp/gcloud.tar.gz --directory /opt  
RUN rm /tmp/gcloud.tar.gz  
  
RUN /opt/google-cloud-sdk/install.sh \  
\--usage-reporting=true \  
\--path-update=true \  
\--bash-completion=true \  
\--rc-path=/etc/profile.d/gcloud.sh  
  
RUN /opt/google-cloud-sdk/bin/gcloud components update  
RUN /opt/google-cloud-sdk/bin/gcloud components install ${GCLOUD_COMPONENTS}  
  
# This is a temporary workaround to make gcloud binaries to be avaliable in
PATH environment variable  
RUN ln -s /opt/google-cloud-sdk/bin/* /usr/local/bin  
  
# Helper scripts  
#COPY scripts/* /usr/local/bin  

