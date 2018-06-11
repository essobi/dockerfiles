FROM ubuntu:xenial  
MAINTAINER Adam Gibbins <adam@adamgibbins.com>  
  
RUN groupadd weechat && \  
useradd --home-dir /weechat --shell /bin/sh --gid weechat weechat && \  
mkdir /weechat && \  
chown -R weechat:weechat /weechat && \  
apt-key adv --keyserver pool.sks-keyservers.net --recv-keys
11E9DE8848F2B65222AA75B8D1820DB22A11534E && \  
echo 'deb http://weechat.org/ubuntu xenial main' >
/etc/apt/sources.list.d/weechat.list && \  
echo 'deb-src http://weechat.org/ubuntu xenial main' >>
/etc/apt/sources.list.d/weechat.list && \  
apt-get update && \  
apt-get install --no-install-recommends --no-install-suggests -y \  
weechat-curses weechat-plugins python-websocket && \  
locale-gen en_GB.UTF-8 && \  
ln -snf /usr/share/zoneinfo/Europe/London /etc/localtime && \  
echo 'Europe/London' > /etc/timezone && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV LANG=en_GB.UTF-8 \  
LANGUAGE=en_GB.UTF-8 \  
LC_ALL=en_GB.UTF-8 \  
C=en_GB.UTF-8 \  
TERM=screen-256color \  
TZ=Europe/London  
  
USER weechat  
VOLUME /weechat  
EXPOSE 9080  
ENTRYPOINT ["weechat"]  

