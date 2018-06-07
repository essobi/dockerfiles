FROM kyero/ruby  
  
LABEL maintainer "Michael Baudino <michael.baudino@alpine-lab.com>"  
  
# Install node from NodeSource (as advised in
https://nodejs.org/en/download/package-manager/)  
# and yarn from the official repository  
RUN buildDependencies=' \  
apt-transport-https \  
' \  
&& apt-get update \  
&& apt-get install -y ${buildDependencies} \  
&& curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
\- \  
&& echo 'deb https://deb.nodesource.com/node_8.x jessie main' >
/etc/apt/sources.list.d/nodesource.list \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" >
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update \  
&& apt-get install -y \--no-install-recommends --no-install-suggests \  
nodejs \  
yarn \  
&& apt-get purge -y \--auto-remove ${buildDependencies} \  
&& rm -rf /var/lib/apt/lists/*  
  
# Use a yarn wrapper as entrypoint.  
# It runs `yarn install` if necessary.  
COPY yarn-wrapper /usr/local/bin/  
ENTRYPOINT ["bundler-wrapper", "yarn-wrapper"]  
CMD ["foreman", "start"]  

