FROM kuzzleio/base  
  
LABEL io.kuzzle.vendor="Kuzzle <support@kuzzle.io>"  
  
WORKDIR /var/app  
ENV TERM=xterm  
  
RUN set -x \  
\  
&& apt-get update && apt-get install -y \  
bash-completion \  
build-essential \  
curl \  
g++ \  
gdb \  
git \  
libfontconfig \  
python \  
rbenv \  
wget \  
&& gem install \  
sass --version 3.2.10 \  
&& npm install -g \  
bower \  
pm2@2.5.0 \  
&& echo "" > /opt/node-v$NODE_VERSION-
linux-x64/lib/node_modules/pm2/lib/keymetrics \  
\  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& echo "alias ll=\"ls -lahF --color\"" >> ~/.bashrc  
  

