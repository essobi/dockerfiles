FROM alpine:edge  
  
RUN apk --update --no-cache add weechat-perl ruby py2-pip python python-dev
build-base py-dbus && \  
pip install --upgrade pip && \  
pip install python-potr && \  
pip install notify2 && \  
apk del python-dev py2-pip build-base  
  
RUN mkdir -p /home/weechat/.weechat && \  
addgroup -S weechat && adduser weechat -D -S -s /sbin/nologin -G weechat
weechat && \  
chown -R weechat:weechat /home/weechat && chmod -R 0755 /home/weechat && \  
weechat --version  
  
USER weechat  
WORKDIR /home/weechat  
ENV HOME /home/weechat  
  
ENTRYPOINT ["weechat"]  

