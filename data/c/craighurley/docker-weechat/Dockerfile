# Run weechat in a container  
# docker run --rm -it -v ~/.weechat:/home/user/.weechat craighurley/docker-
weechat  
FROM alpine:edge  
MAINTAINER Craig Hurley  
  
ENV LANG C.UTF-8  
ENV TERM xterm-256color  
ENV HOME /home/user  
  
RUN apk add \--no-cache \  
weechat \  
weechat-perl \  
weechat-python \  
weechat-aspell \  
ca-certificates \  
aspell-en \  
ncurses \  
python \  
perl  
  
RUN adduser -D -h $HOME user \  
&& mkdir -p $HOME/.weechat \  
&& chown -R user:user $HOME  
  
WORKDIR $HOME  
  
VOLUME [ "$HOME/.weechat" ]  
  
USER  user  
  
ENTRYPOINT [ "weechat" ]  

