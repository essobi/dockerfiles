FROM node:7.1  
MAINTAINER Jonathan Hawk <jonathan@appertly.com>  
  
RUN npm install --global broccoli-cli broccoli-uglify-sourcemap \  
&& npm install --global doublecompile/broccoli-timepiece#feature-broccoli-1.0
\  
&& git config --system user.name Docker \  
&& git config --system user.email docker@localhost \  
&& rm -rf /tmp/* /var/tmp/* \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/log/apt/* \  
&& rm -rf /var/log/dpkg.log \  
&& rm -rf /var/log/bootstrap.log \  
&& rm -rf /var/log/alternatives.log  
  
VOLUME ["/opt/broccoli/project"]  
WORKDIR /opt/broccoli/project  
ENTRYPOINT ["/usr/local/bin/broccoli-timepiece"]  
CMD ["dist"]  

