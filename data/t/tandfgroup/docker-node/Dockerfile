FROM node:9  
  
ENV NODE_VERSION 9.4.0  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
curl \  
git \  
openssh-client \  
openssh-server \  
&& rm -rf /var/lib/apt/lists/* \  
&& npm i -g \  
bower \  
gulp \  
karma-cli \  
# node-sass \  
pm2 \  
protractor \  
typescript \  
typings \  
webpack \  
webpack-dev-server \  
&& npm cache clean -g -f \  
&& git clone --depth=1 https://github.com/docker/docker-bench-security.git
/docker-bench-security && rm -rf !$/.git \  
&& chmod -R 755 /docker-bench-security  

