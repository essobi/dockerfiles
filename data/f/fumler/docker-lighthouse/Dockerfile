FROM debian:sid  
  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
ca-certificates \  
curl \  
gnupg \  
\--no-install-recommends \  
&& curl -sSL https://deb.nodesource.com/setup_6.x | bash - \  
&& curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add
\- \  
&& echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main"
> /etc/apt/sources.list.d/google-chrome.list \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update && apt-get install -y \  
yarn \  
jq \  
rsync \  
google-chrome-stable \  
nodejs \  
\--no-install-recommends \  
&& apt-get purge --auto-remove -y gnupg \  
&& rm -rf /var/lib/apt/lists/*  
  
ARG CACHEBUST=1  
RUN yarn global add lighthouse@next

