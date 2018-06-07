FROM docker:latest  
  
MAINTAINER Dmitriy Ansimov "d.ansimov@owox.com"  
RUN \  
apk add --no-cache curl python py-pip mariadb-client openssh-client git
gettext && \  
rm -rf /var/cache/apk/* && \  
pip install --no-cache-dir docker-compose  
  
RUN \  
curl https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz >
/tmp/google-cloud-sdk.tar.gz && \  
mkdir -p /usr/local/gcloud && \  
tar -C /usr/local/gcloud -xvf /tmp/google-cloud-sdk.tar.gz && \  
rm -f /tmp/google-cloud-sdk.tar.gz && \  
/usr/local/gcloud/google-cloud-sdk/install.sh --usage-reporting=true \--path-
update=true \--bash-completion=true \--rc-path=/root/.bashrc --additional-
components app-engine-java app-engine-python app kubectl alpha beta gcd-
emulator pubsub-emulator cloud-datastore-emulator app-engine-go bigtable && \  
/usr/local/gcloud/google-cloud-sdk/bin/gcloud config set \--installation
component_manager/disable_update_check true && \  
sed -i -- 's/\"disable_updater\": false/\"disable_updater\": true/g'
/usr/local/gcloud/google-cloud-sdk/lib/googlecloudsdk/core/config.json  
  
ENV PATH=$PATH:/usr/local/gcloud/google-cloud-sdk/bin  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["sh"]  

