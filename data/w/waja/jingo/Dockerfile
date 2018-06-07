FROM mhart/alpine-node:latest  
  
# Dockerfile Maintainer  
MAINTAINER Jan Wagner "waja@cyconet.org"  
ARG "BUILD_DATE=unknown"  
ARG "BUILD_VERSION=unknown"  
ARG "VCS_URL=unknown"  
ARG "VCS_REF=unknown"  
ARG "VCS_BRANCH=unknown"  
# See http://label-schema.org/rc1/ and https://microbadger.com/labels  
LABEL org.label-schema.name="jingo - Node.js based Wiki" \  
org.label-schema.description="Git based wiki engine written for node.js, with
a decent design, a search capability and a good typography on Alpine Linux
based container" \  
org.label-schema.vendor="Cyconet" \  
org.label-schema.schema-version="1.0" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.version=$BUILD_VERSION \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-branch=$VCS_BRANCH  
  
# Install dependencies  
RUN apk --no-cache add --virtual build-dependencies git ca-certificates && \  
# Pull jingo source  
git clone https://github.com/claudioc/jingo.git /opt/jingo && cd /opt/jingo &&
\  
# Checkout latest tag  
LATEST_TAG=$(git tag -l 'v*.[0-9]' \--sort='v:refname'| tail -1); git checkout
$LATEST_TAG -b $LATEST_TAG && \  
# Set global git config  
git config --global user.name "Jingo Wiki" && git config --global user.email
"everyone@jingo" && \  
# Install npm depenencies  
npm install && \  
# Adjust configuration path in package.json script  
sed -ri 's#"./jingo -c config.yaml"#"./jingo -c config/config.yaml"#'
/opt/jingo/package.json && \  
# Create configuration dir  
mkdir -p /opt/jingo/config  
  
WORKDIR /opt/jingo  
ADD start.sh /opt/jingo/start.sh  
CMD /bin/sh /opt/jingo/start.sh  

