FROM postgres:latest  
  
# backups to Google Storage  
RUN apt-get update \  
&& apt-get install -y wget unzip python cron \  
&& rm -rf /var/lib/apt/lists/*  
  
# download google cloud-sdk  
RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip
&& unzip google-cloud-sdk.zip && rm google-cloud-sdk.zip  
  
# install minimal google cloud-sdk  
RUN google-cloud-sdk/install.sh --usage-reporting=true \--path-update=true
\--bash-completion=true \--rc-path=/.bashrc  
  
# Disable updater check for the whole installation.  
RUN google-cloud-sdk/bin/gcloud config set \--installation
component_manager/disable_update_check true  
  
# Disable updater completely.  
RUN sed -i -- 's/\"disable_updater\": false/\"disable_updater\": true/g'
/google-cloud-sdk/lib/googlecloudsdk/core/config.json  
  
# add gce cli to PATH  
ENV PATH /google-cloud-sdk/bin:$PATH  
  
# entrypoint  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD touch /var/log/cron.log && cron && tail -f /var/log/cron.log  

