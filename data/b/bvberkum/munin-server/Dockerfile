ARG BASE_TAG=xenial  
FROM ubuntu:$BASE_TAG  
MAINTAINER B. van Berkum <dev@dotmpe.com>  
  
LABEL \  
description="bvberkum/docker-munin-server forked from Scalingo/docker-munin-
server" \  
urls.hub=https://hub.docker.com/r/bvberkum/docker-munin-server \  
urls.repo=https://github.com/bvberkum/munin-server  
  
RUN adduser --system --home /var/lib/munin --shell /bin/false \--uid 1103
--group munin  
  
RUN apt-get update -qq && RUNLEVEL=1 DEBIAN_FRONTEND=noninteractive \  
apt-get install -y -qq \  
openssh-client rsyslog cron munin munin-node nginx \  
wget heirloom-mailx patch spawn-fcgi libcgi-fast-perl curl  
RUN rm /etc/nginx/sites-enabled/default && \  
mkdir -p /var/cache/munin/www && \  
chown munin:munin /var/cache/munin/www && \  
mkdir -p /var/run/munin && \  
chown -R munin:munin /var/run/munin  
  
VOLUME /var/lib/munin  
VOLUME /var/log/munin  
  
ADD ./munin.conf /etc/munin/munin.conf  
ADD ./nginx.conf /etc/nginx/nginx.conf  
ADD ./nginx-munin /etc/nginx/sites-enabled/munin  
ADD ./start-munin.sh /munin  
ADD ./munin-graph-logging.patch /usr/share/munin  
ADD ./munin-update-logging.patch /usr/share/munin  
  
RUN cd /usr/share/munin \  
&& patch munin-graph < munin-graph-logging.patch \  
&& patch munin-update < munin-update-logging.patch  
  
ADD ./check-munin.sh /check  
ENV HEALTH_HOSTINFO=  
ENV HEALTH_CHECK_NODES=1  
HEALTHCHECK \--interval=5m --timeout=10s --retries=3 CMD /check || exit 1  
  
EXPOSE 8080  
CMD ["bash", "/munin"]  

