FROM ruby:2.3  
RUN apt-get update  
  
# DEBIAN_DPKGS BEGIN  
RUN set -ex \  
&& apt-get install -y --no-install-recommends ca-certificates curl wget git-
core htop screen apt-transport-https vim logrotate  
  
# DEBIAN_DPKGS END  
# SUPERVISOR BEGIN  
RUN set -ex \  
&& apt-get install -y --no-install-recommends supervisor \  
&& mkdir -p /var/log/supervisor \  
&& { \  
echo '[supervisord]'; \  
echo 'nodaemon=true'; \  
} >> /etc/supervisor/conf.d/supervisord.conf  
  
# SUPERVISOR END  
# CRON_SERVER BEGIN  
RUN set -ex \  
&& apt-get install -y --no-install-recommends cron \  
&& { \  
echo '[program:cron]'; \  
echo 'command=/usr/sbin/cron -f'; \  
} >> /etc/supervisor/conf.d/cron.conf  
  
# CRON_SERVER END  
# LOCALE BEGIN  
RUN set -ex \  
&& apt-get install -y --no-install-recommends locales \  
&& echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \  
&& locale-gen \  
&& update-locale LANG=en_US.UTF-8 LANGUAGE=en_US:en:  
  
ENV LC_ALL en_US.UTF-8  
# LOCALE END  
# TIMEZONE BEGIN  
RUN set -ex \  
&& echo "Asia/Shanghai" > /etc/timezone \  
&& dpkg-reconfigure -f noninteractive tzdata  
  
# TIMEZONE END  
# GEMS BEGIN  
RUN set -ex \  
  
&& gem install backup -v '~> 4.4' \  
  
&& gem install whenever \  
  
&& echo 'done' > /dev/null  
# GEMS END  
# DEBIAN_CLEAN BEGIN  
RUN set -ex \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# DEBIAN_CLEAN END  
# DOTBASHRC BEGIN  
RUN set -ex \  
&& { \  
echo "export TERM=xterm"; \  
echo "export PATH=$(echo $PATH)"; \  
} >> /root/.bashrc  
  
# DOTBASHRC END  
WORKDIR /root  
  
CMD ["sh", "-c", "env > /etc/environment ; /usr/bin/supervisord"]

