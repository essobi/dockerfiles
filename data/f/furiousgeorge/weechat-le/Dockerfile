FROM ubuntu:16.04  
MAINTAINER Furious George <furiousgeorgecode@gmail.com>  
  
ENV APTLIST="git openssl ca-certificates letsencrypt supervisor weechat
weechat-curses weechat-plugins weechat-scripts"  
ENV TERM xterm-256color  
  
RUN apt-get update && apt-get install -qq -y --no-install-recommends $APTLIST
&& apt-get clean  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
CMD ["/run.sh"]  

