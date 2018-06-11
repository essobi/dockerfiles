FROM node:8.2.1  
MAINTAINER Tibor Sári <tiborsari@gmx.de>  
  
RUN \  
apt-get update -qq && \  
apt-get install --no-install-recommends -y \  
apt-transport-https \  
&& curl -sS "https://dl.yarnpkg.com/debian/pubkey.gpg" | apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update -qq \  
&& apt-get install --no-install-recommends -y \  
sudo \  
yarn \  
&& \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir ~/.npm-global && chown node.node ~/.npm-global  
ENV NPM_CONFIG_PREFIX=~/.npm-global  
  
# Set up the application directory  
VOLUME ["/app"]  
WORKDIR /app  
  
ADD node-init.sh /usr/local/bin/node-init.sh  
ADD https://raw.githubusercontent.com/tsari/docker-
entrypoint/master/entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh && chmod +x /usr/local/bin/node-
init.sh  
  
# Set up the command arguments  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
CMD [ "node", "-v" ]

