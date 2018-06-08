FROM skegio/base  
  
RUN apt-get update && apt-get install apt-transport-https language-pack-en
python-pip -y  
  
# wee-chat  
RUN apt-key adv --keyserver pool.sks-keyservers.net --recv-keys
11E9DE8848F2B65222AA75B8D1820DB22A11534E && \  
echo "deb https://weechat.org/ubuntu xenial main"
>/etc/apt/sources.list.d/weechat.list && \  
echo "deb-src https://weechat.org/ubuntu xenial main"
>>/etc/apt/sources.list.d/weechat.list && \  
apt-get update && \  
apt-get install -y weechat-curses weechat-plugins perl  
  
# required for the wee-slack plugin  
RUN pip install websocket-client  
  
RUN apt-get update && apt-get install bitlbee bitlbee-plugin-otr perl -y  

