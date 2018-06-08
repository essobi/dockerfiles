FROM ruby:2.2.5  
# DEBIAN_MIRROR BEGIN  
RUN set -ex \  
&& sed -i 's/security.debian.org/mirrors.aliyun.com\/debian-security/g'
/etc/apt/sources.list \  
&& sed -i 's/httpredir.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list
\  
&& apt-get update  
  
# DEBIAN_MIRROR END  
# DEBIAN_DPKGS BEGIN  
RUN set -ex \  
&& apt-get install -y --no-install-recommends ca-certificates curl wget git-
core htop screen apt-transport-https vim  
  
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
# SSH_SERVER BEGIN  
RUN set -ex \  
&& apt-get install -y --no-install-recommends openssh-server \  
&& mkdir -p /var/run/sshd \  
&& { \  
echo '[program:sshd]'; \  
echo 'command=/usr/sbin/sshd -D'; \  
} >> /etc/supervisor/conf.d/sshd.conf  
  
# SSH_SERVER END  
# CRON_SERVER BEGIN  
RUN set -ex \  
&& apt-get install -y --no-install-recommends cron \  
&& { \  
echo '[program:cron]'; \  
echo 'command=/usr/sbin/cron -f'; \  
} >> /etc/supervisor/conf.d/cron.conf  
  
# CRON_SERVER END  
# NGINX_SERVER BEGIN  
RUN apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \  
&& echo "deb http://nginx.org/packages/debian/ $(awk -F"[)(]+" '/VERSION=/
{print $2}' /etc/os-release) nginx" >> /etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates \  
nginx \  
&& { \  
echo '[program:nginx]'; \  
echo 'command=nginx -g "daemon off;"'; \  
} >> /etc/supervisor/conf.d/nginx.conf  
  
# NGINX_SERVER END  
# NODE6 BEGIN  
ENV NODE_VERSION 6.2.2  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_HOME /usr/local/node  
ENV NODE_BIN="$NODE_HOME/bin"  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& mkdir -p "$NODE_HOME" \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C "$NODE_HOME" --strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt  
  
ENV PATH $NODE_BIN:$PATH  
  
# NODE6 END  
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
# SSH_AGENT BEGIN  
RUN set -ex \  
&& mkdir -p /root/.ssh /root/.bash.d \  
&& { \  
echo 'Host *'; \  
echo 'ServerAliveInterval=15'; \  
echo 'ServerAliveCountMax=6'; \  
echo 'ForwardAgent yes'; \  
} >> /root/.ssh/config \  
&& { \  
echo 'source ~/.bash.d/10_ssh-agent.bash'; \  
} >> /root/.bashrc  
  
RUN set -ex \  
&& cd /root/.bash.d \  
&& curl -SLO https://raw.githubusercontent.com/agideo/docker-
baseimage/master/files/bash.d/10_ssh-agent.bash \  
&& cd -  
  
# SSH_AGENT END  
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
RUN mkdir /app  
WORKDIR /app  
VOLUME /app  
  
EXPOSE 22 80  
CMD ["/usr/bin/supervisord"]

