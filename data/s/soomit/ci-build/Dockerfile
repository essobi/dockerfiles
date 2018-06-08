FROM node:8-stretch  
LABEL name="ci-build" \  
maintainer="Cédric Reginster <cedric.reginster@soom-it.ch>" \  
version="1.0" \  
description="Official Node.js (v8), Google Chrome (Stable), AWS cli, git, apex
up"  
  
# Install google chrome & build tools (awscli & nomad).  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip" \  
&& wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add \- \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update \  
&& apt-get install -y unzip python-dev git google-chrome-stable \  
&& unzip awscli-bundle.zip \  
&& ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws \  
&& curl -sf https://up.apex.sh/install | sh \  
&& rm awscli-bundle.zip \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/* \  
&& touch /tmp/build.log && ln -sfT /dev/stderr /tmp/build.log  
  
# Default chrome debug port  
EXPOSE 9222  
  
CMD [ "node" ]  

