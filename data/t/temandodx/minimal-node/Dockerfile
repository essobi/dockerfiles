FROM node:4.7-alpine  
  
ENV NPM_CONFIG_LOGLEVEL="warn"  
ARG SOURCE_TYPE="Git"  
ARG SOURCE_URL="https://github.com/temando/docker-minimal-node"  
ARG SOURCE_COMMIT  
LABEL com.temando.name="docker-minimal-node" \  
com.temando.description="Minimal docker image installing node modules." \  
com.temando.vendor="Temando Pty Ltd" \  
com.temando.vcs-type=$SOURCE_TYPE \  
com.temando.vcs-url=$SOURCE_URL \  
com.temando.vcs-ref=$SOURCE_COMMIT  
# Install:  
# - Latest npm (not bundled version).  
# - Yarn via NPM until official package for Alpine linux is ready.  
RUN npm set registry "http://registry.npmjs.org" \  
&& npm install --global npm \  
&& npm install --global yarn \  
&& npm cache clean  

