FROM ubuntu-debootstrap:14.04  
MAINTAINER Peter Rosell <peter.rosell@gmail.com>  
  
# Install packages required  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y wget cron \  
python python-dev python-yaml python-simplejson python-pip \  
librsync-dev ncftp lftp rsync  
  
# Install the pyhton requirements  
ADD assets/requirements.txt /tmp/  
RUN pip install --upgrade --requirement /tmp/requirements.txt  
  
ENV GOOGLE_AUTH_MODE personal  
ENV GOOGLE_SECRETS_FILE /config/client_secret.json  
ENV GOOGLE_CREDENTIALS_FILE /keys/client_credentials.json  
  
ENV ENCRYPTION_ALGORITHM AES256  
ENV DEST_URL pydrive://user@gmail.com/backup  
ENV CRON_EXPR 0 5 * * *  
ENV FULL_BACKUP_INTERVAL 7D  
  
VOLUME /data  
VOLUME /keys  
VOLUME /cache  
  
ADD assets/* /tmp/  
  
RUN ln -s /config ~/.gnupg  
RUN mkdir ~/.cache  
RUN ln -s /cache ~/.cache/duplicity  
  
# Download and install duplicity  
RUN export VERSION=0.7.02 && \  
cd /tmp/ && \  
wget -qO -
https://launchpad.net/duplicity/0.7-series/$VERSION/+download/duplicity-$VERSION.tar.gz
\  
| tar xz && \  
cd duplicity-$VERSION && \  
patch -p1 < ../duplicity.patch && \  
./setup.py install  
  
ADD config /config  
ADD bin/* /usr/local/bin/  
  
# Set the ENTRYPOINT  
ENTRYPOINT [ "/usr/local/bin/backup.sh" ]  
CMD [ "backup-cronjob" ]

