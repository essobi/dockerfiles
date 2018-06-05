FROM debian:jessie  
MAINTAINER Thyago Almeida <thyagoaa@gmail.com>  
  
# explicitly set user/group IDs (like Official PostgreSQL docker does)  
RUN groupadd -r postgres --gid=999 && useradd -r -s /bin/bash -g postgres
--uid=999 postgres  
  
# install cron, ssh, rsync and supervisor  
RUN \  
apt-get update && \  
apt-get install -y cron && \  
apt-get install -y openssh-server && \  
apt-get install -y rsync && \  
apt-get install -y supervisor && \  
sed -ri 's/#AuthorizedKeysFile/AuthorizedKeysFile/g' /etc/ssh/sshd_config && \  
sed -ri 's/#PasswordAuthentication yes/PasswordAuthentication no/g'
/etc/ssh/sshd_config && \  
mkdir -p /var/lib/postgresql/.ssh && \  
chown postgres /var/lib/postgresql/.ssh && \  
usermod -d /var/lib/postgresql postgres && \  
mkdir -p /var/run/sshd && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY ./build/docker-entrypoint.sh /  
COPY ./build/archiver/archive.sh /archiver/bin/  
COPY ./build/cron/archive /etc/cron.d/  
COPY ./build/supervisor/supervisord.conf /etc/supervisor/conf.d/  
  
EXPOSE 22  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["supervisord"]

