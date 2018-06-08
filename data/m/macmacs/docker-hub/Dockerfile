# Cloud9 server  
# A lot inspired by https://hub.docker.com/r/gai00/cloud9/~/dockerfile/  
# https://hub.docker.com/r/kdelfour/cloud9-docker/~/dockerfile/  
  
FROM node:6-slim  
#FROM node:0.10-slim  
MAINTAINER MacMacs <2017@macmacs.com>  
  
RUN buildDeps='make build-essential g++ gcc python2.7' && softDeps="git util-
linux bash" \  
&& apt-get update && apt-get upgrade -y \  
&& apt-get install -y tmux graphicsmagick ssh nano vnstat htop php5-cli zip
locales $buildDeps $softDeps --no-install-recommends \  
&& npm install -g forever && npm cache clean \  
&& git clone https://github.com/c9/core.git /cloud9 && cd /cloud9 \  
&& scripts/install-sdk.sh \  
&& curl https://install.meteor.com/ | sh \  
&& locale-gen en_US.UTF-8 \  
&& localedef -i en_GB -f UTF-8 en_US.UTF-8 \  
&& apt-get autoremove -y && apt-get autoclean -y && apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& npm cache clean  
  
VOLUME /workspace  
EXPOSE 8181  
ENTRYPOINT ["forever", "/cloud9/server.js", "-w", "/workspace", "-l",
"0.0.0.0"]  
  
#CMD["--auth","username:password"]  

