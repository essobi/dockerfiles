#  
# Ruby backup gem service docker image  
#  
# http://github.com/tenstartups/backup-service-docker  
#  
  
FROM tenstartups/alpine:latest  
  
LABEL maintainer="Marc Lennox <marc.lennox@gmail.com>"  
# Set environment variables.  
ENV \  
HOME=/home/backups \  
BACKUP_CONFIG_DIR=/etc/backups \  
BACKUP_DATA_DIR=/var/lib/backups  
  
# Install base packages.  
RUN \  
apk --update add \  
build-base \  
libressl-dev \  
libxml2-dev \  
libxslt-dev \  
mysql-client \  
postgresql \  
readline-dev \  
redis \  
ruby \  
ruby-bigdecimal \  
ruby-bundler \  
ruby-dev \  
ruby-irb \  
ruby-io-console \  
ruby-json \  
ruby-nokogiri \  
ruby-rake \  
sqlite \  
tar \  
zlib-dev && \  
rm -rf /var/cache/apk/*  
  
# Install ruby gems.  
RUN \  
gem install backup --no-document \--version=5.0.0.beta.1  
# Define working directory.  
WORKDIR /home/backups  
  
# Define mountable directories.  
VOLUME ["/home/backups", "/etc/backups", "/var/lib/backups",
"/var/log/backups"]  
  
# Add files to the container.  
COPY entrypoint.sh /docker-entrypoint  
COPY perform-backup.sh /usr/local/bin/perform-backup  
  
# Set the entrypoint script.  
ENTRYPOINT ["/docker-entrypoint"]  

