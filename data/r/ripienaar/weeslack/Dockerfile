FROM debian:stretch  
  
ENV TERM=screen-256color  
ENV LANG=C.UTF-8  
ENV UID=1000  
ENV GID=1000  
RUN apt-get update && \  
apt-get install -y apt-transport-https gnupg && \  
apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
11E9DE8848F2B65222AA75B8D1820DB22A11534E && \  
echo 'deb https://weechat.org/debian stretch main'
>/etc/apt/sources.list.d/weechat.list && \  
apt-get update && \  
apt-get install -y weechat-curses weechat-plugins python-pip aspell aspell-en
aspell-uk && \  
pip install websocket-client && \  
groupadd --gid ${GID} weechat && \  
adduser --uid ${UID} \--gid ${GID} weechat --no-create-home --home /weechat
--disabled-password --gecos weechat && \  
rm -rf /var/lib/apt/lists/*  
  
VOLUME /weechat  
  
WORKDIR /weechat  
  
USER weechat  
  
EXPOSE 9001  
ENTRYPOINT ["/usr/bin/weechat"]  
CMD ["--dir /weechat"]  

