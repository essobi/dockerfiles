FROM moul/tmux  
MAINTAINER Manfred Touron m@42.am  
  
# Inspired by https://github.com/creack/weechat-docker/blob/master/Dockerfile  
RUN apt-get update && \  
apt-get -qq -y install python-software-properties && \  
add-apt-repository ppa:nesthib/weechat-stable && \  
apt-get -qq -y update && \  
apt-get clean  
  
ENV TERM screen-256color  
ENV LANG C.UTF-8  
RUN apt-get -qq -y install weechat && \  
apt-get clean  
  
RUN useradd -m -d /weechat weechat  
ADD command /root/command  
ADD http://www.weechat.org/files/scripts/weeget.py /weechat/.weechat/python/  
RUN mkdir -p /weechat/.weechat/python/autoload && \  
ln -s /weechat/.weechat/python/weeget.py
/weechat/.weechat/python/autoload/weeget.py  
  
#VOLUME ["/weechat"]  
EXPOSE 8000 8001 8002  
CMD ["run-docker-tmux"]  

