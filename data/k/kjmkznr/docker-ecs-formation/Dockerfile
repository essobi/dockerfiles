FROM golang:alpine  
MAINTAINER KOJIMA Kazunori <kjm.kznr@gmail.com>  
  
WORKDIR /  
  
ENV ENTRYKIT_VERSION 0.4.0  
# Install Entrykit  
RUN apk --update add openssl \  
&& rm -rf /var/cache/apk/* \  
&& wget
https://github.com/progrium/entrykit/releases/download/v${ENTRYKIT_VERSION}/entrykit_${ENTRYKIT_VERSION}_Linux_x86_64.tgz
\  
&& tar -xvzf entrykit_${ENTRYKIT_VERSION}_Linux_x86_64.tgz \  
&& rm entrykit_${ENTRYKIT_VERSION}_Linux_x86_64.tgz \  
&& mv entrykit /bin/entrykit \  
&& chmod +x /bin/entrykit \  
&& entrykit --symlink  
  
# Install ecs-formation  
RUN apk --update add git \  
&& rm -rf /var/cache/apk/* \  
&& go get github.com/stormcat24/ecs-formation  
  

