FROM mhart/alpine-node:latest  
  
# Dockerfile Maintainer  
MAINTAINER Thomas M. Schaedler "thomas@lambda.li"  
# Install dependencies  
RUN apk --no-cache add --virtual build-dependencies git ca-certificates \  
# Pull jingo source  
&& git clone https://github.com/claudioc/jingo.git /opt/jingo \  
&& cd /opt/jingo \  
# Checkout latest tag  
&& LATEST_TAG=$(git tag -l 'v*.[0-9]' \--sort='v:refname'| tail -1); git
checkout $LATEST_TAG -b $LATEST_TAG \  
# Set global git config  
&& git config --global user.name "Jingo Wiki" && git config --global
user.email "everyone@jingo" \  
# Install npm depenencies  
&& npm install \  
# Adjust configuration path in package.json script  
&& sed -ri 's#"./jingo -c config.yaml"#"./jingo -c config/config.yaml"#'
/opt/jingo/package.json \  
# Create configuration dir where you MUST map your config at (see templates)  
&& mkdir -p /opt/jingo/config  
  
WORKDIR /opt/jingo  
ENTRYPOINT ["npm","start"]

