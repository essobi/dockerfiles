FROM debian:stretch-slim  
  
RUN echo 'deb http://deb.debian.org/debian stretch main contrib non-free'
>/etc/apt/sources.list  
RUN echo 'deb http://security.debian.org/debian-security/ stretch/updates main
contrib non-free' >>/etc/apt/sources.list  
RUN echo 'deb http://deb.debian.org/debian stretch-updates main contrib non-
free' >>/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y autoconf \  
curl \  
vim \  
unzip  
  
WORKDIR /data  
ADD . /data/  
  
RUN chmod 755 /data/ChatScriptNLP/BINARIES/LinuxChatScript64  
  
RUN { echo '#!/bin/bash'; \  
echo 'set -e'; \  
echo 'cd /data/ChatScriptNLP/BINARIES'; \  
echo './LinuxChatScript64' \  
'source=/data/sourceBot.txt' \  
'livedata=/data/ChatScriptNLP/LIVEDATA' \  
'topic=/data/ChatScriptNLP/TOPIC' \  
'users=/data/ChatScriptNLP/USERS' \  
'logs=/data/ChatScriptNLP/LOGS' \  
'tmp=/data/ChatScriptNLP/TMP'; \  
} > /entrypoint-chatscript.sh \  
&& chmod +x /entrypoint-chatscript.sh  
  
ENV PORT 1024  
ENV DEBIAN_FRONTEND noninteractive  
  
EXPOSE 1024  
# startup  
USER root  
  
CMD ["/bin/echo", "Hello ChatScript"]  
CMD ["/entrypoint-chatscript.sh"]  

