ARG DOCKER_TAG=latest  
FROM nouchka/symfony:${DOCKER_TAG}  
LABEL maintainer docker@katagena.com  
  
ARG PHPVERSION=5  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
[ "$PHPVERSION" != "5" ] || apt-get -yq install npm && ln -s /usr/bin/nodejs
/usr/bin/node && \  
[ "$PHPVERSION" != "7.0" ] || apt-get install -yq gnupg && curl -sL
https://deb.nodesource.com/setup_6.x | bash - && apt-get install -yq nodejs &&
\  
npm install -g bower && \  
npm install -g less && \  
npm install -g uglify-js && \  
npm install -g uglifycss && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

