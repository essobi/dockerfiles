ARG NODE_VERSION=10  
FROM node:$NODE_VERSION  
  
LABEL authors="cris barbero <cfbarbero@gmail.com>"  
  
# Install google chrome and cleanup the apt-cache  
RUN curl https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
\  
&& sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list' \  
&& apt-get update \  
&& apt-get install -y google-chrome-stable \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# We need to install angular CLI globally so that we can use it in our build
scripts  
# unsafe-perm is needed because root doesn't have access to the .node-gyp
folder in node image (https://github.com/nodejs/node-gyp/issues/454)  
ARG NG_CLI_VERSION=1.7.4  
ENV NG_CLI_VERSION=$NG_CLI_VERSION  
RUN npm update && npm install --unsafe-perm -g @angular/cli@$NG_CLI_VERSION

