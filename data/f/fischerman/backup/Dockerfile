FROM ubuntu:17.04  
  
RUN apt-get update && apt-get install -y rsync rdiff-backup curl postgresql-
client-9.6 bc openssh-client  
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl
-s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl && \  
chmod +x ./kubectl && \  
mv ./kubectl /usr/local/bin/kubectl && \  
pg_dump \--version  
ADD backup-nextcloud.sh /  
RUN chmod +x /backup-nextcloud.sh

