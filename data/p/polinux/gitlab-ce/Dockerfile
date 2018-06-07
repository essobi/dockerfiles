FROM ubuntu:16.04  
SHELL ["/bin/sh", "-c"],  
  
ENV \  
BACKUP_TIME="0 12 * * *" \  
PATH=/opt/gitlab/embedded/bin:/opt/gitlab/bin:/assets:$PATH \  
TERM=xterm \  
PACKAGECLOUD_REPO=gitlab-ce \  
RELEASE_PACKAGE=gitlab-ce \  
RELEASE_VERSION=10.3.1-ce.0 \  
DOWNLOAD_URL=https://downloads-packages.s3.amazonaws.com/ubuntu-xenial/gitlab-
ce_10.3.1-ce.0_amd64.deb  
  
COPY container-files /  
  
RUN \  
apt-get update -q && \  
DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends \  
ca-certificates \  
openssh-server \  
wget \  
apt-transport-https \  
vim \  
tzdata \  
cron \  
nano && \  
rm -rf /var/lib/apt/lists/* && \  
sed 's/session\s*required\s*pam_loginuid.so/session optional
pam_loginuid.so/g' -i /etc/pam.d/sshd && \  
rm -rf /etc/update-motd.d /etc/motd /etc/motd.dynamic && \  
ln -fs /dev/null /run/motd. && \  
/assets/setup  
  
EXPOSE 443 80 22  
VOLUME ["/etc/gitlab", "/var/opt/gitlab", "/var/log/gitlab"]  
  
CMD ["/assets/wrapper"]  
  
HEALTHCHECK \--interval=60s --timeout=30s --retries=5 \  
CMD /opt/gitlab/bin/gitlab-healthcheck --fail  

