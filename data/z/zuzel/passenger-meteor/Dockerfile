FROM ubuntu:14.04  
  
MAINTAINER Ivan Suslov <digitalzuzel@gmail.com>  
  
RUN NODE_VERSION=0.10.44 && NODE_ARCH=x64 \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys
561F9B9CAC40B2F7 \  
&& apt-get update \  
&& apt-get install -y wget cups apt-transport-https ca-certificates \  
&& sh -c 'echo deb https://oss-binaries.phusionpassenger.com/apt/passenger
trusty main > /etc/apt/sources.list.d/passenger.list' \  
&& apt-get update \  
&& apt-get install -y nginx-extras passenger build-essential libssl-dev git
python rpl \  
&& NODE_DIST=node-v${NODE_VERSION}-linux-${NODE_ARCH} \  
&& cd /tmp \  
&& wget http://nodejs.org/dist/v${NODE_VERSION}/${NODE_DIST}.tar.gz \  
&& tar xvzf ${NODE_DIST}.tar.gz \  
&& rm -rf /opt/nodejs \  
&& mv ${NODE_DIST} /opt/nodejs \  
&& ln -sf /opt/nodejs/bin/node /usr/bin/node && ln -sf /opt/nodejs/bin/npm
/usr/bin/npm \  
&& npm install -g node-gyp \  
&& node-gyp install ${NODE_VERSION} && npm install fibers@1.0.5  
  
RUN rpl '# passenger_root' 'passenger_root' /etc/nginx/nginx.conf \  
&& rpl '# passenger_ruby' 'passenger_ruby' /etc/nginx/nginx.conf \  
&& apt-get update \  
&& apt-get upgrade -y  
  
  
COPY ./init-apps.sh /  
ENTRYPOINT ["/init-apps.sh"]  
  

