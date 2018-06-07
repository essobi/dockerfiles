FROM unit9/cron:latest  
MAINTAINER Kamil Cholewiński <kamil.cholewinski@unit9.com>  
  
RUN echo 'deb http://cdn.debian.net/debian/ jessie-backports main' \  
> /etc/apt/sources.list.d/jessie-backports.list  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive \  
apt-get install --no-install-recommends --yes \  
postgresql-client-9.6/jessie-backports \  
python \  
&& rm -rf /var/cache/apt /var/lib/apt/lists  
  
RUN set -x \  
&& curl -fsS -o /tmp/sdk.tar.gz \  
https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.tar.gz \  
&& cd /opt \  
&& tar zxf /tmp/sdk.tar.gz \  
&& rm /tmp/sdk.tar.gz \  
&& google-cloud-sdk/install.sh --quiet \  
&& ln -s /opt/google-cloud-sdk/bin/gcloud /usr/local/bin/gcloud \  
&& gcloud \--quiet config set disable_usage_reporting true \  
&& gcloud \--quiet components install \  
gsutil \  
&& ln -s /opt/google-cloud-sdk/bin/gsutil /usr/local/bin/gsutil \  
&& mv /root/.bashrc.backup /root/.bashrc \  
&& gcloud \--version \  
&& gsutil \--version \  
&& true  
  
ENV PGUSER="postgres" \  
PGPASSWORD="postgres" \  
PGHOST="postgres" \  
PGPORT="5432" \  
BOTO_PATH="" \  
GS_PATH="" \  
GOOGLE_APPLICATION_CREDENTIALS=""  
  
ADD dumper.cron /etc/cron.daily/50-dumper  
ADD uploader.cron /etc/cron.daily/60-uploader  
ADD rc.local /etc/rc.local  
VOLUME /var/backups  

