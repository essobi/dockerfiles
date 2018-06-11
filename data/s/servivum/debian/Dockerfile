# Debian Docker Base Image with Useful Tools  
FROM debian:jessie  
MAINTAINER Patrick Baber <patrick.baber@servivum.com>  
  
# Install utilities  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
cron \  
curl \  
git \  
nano \  
openssh-server \  
rsync \  
ssmtp \  
supervisor \  
unzip \  
vim \  
wget && \  
  
# Clean up  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Configure Supervisor  
COPY etc/supervisor/supervisord.conf /etc/supervisor/supervisord.conf  
  
# Configure SSH  
ENV NOTVISIBLE "in users profile"  
COPY etc/supervisor/conf.d/sshd.conf /etc/supervisor/conf.d/sshd.conf  
RUN mkdir -p /var/run/sshd && \  
mkdir /root/.ssh && \  
sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd && \  
echo "export VISIBLE=now" >> /etc/profile  
  
# Configure cron  
# @TODO: Configure cron  
# https://github.com/mailtank-ru/rsstank/blob/master/docker/files/cron-
supervisor.conf  
# https://www.ekito.fr/people/run-a-cron-job-with-docker/  
COPY etc/supervisor/conf.d/cron.conf /etc/supervisor/conf.d/cron.conf  
  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 22  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]

