FROM debian:sid  
  
# Install necessary dependencies to get lighthouse working.  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
ca-certificates \  
build-essential \  
curl \  
gnupg \  
\--no-install-recommends \  
&& curl -sSL https://deb.nodesource.com/setup_6.x | bash - \  
&& curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add
\- \  
&& echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main"
> /etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update && apt-get install -y \  
google-chrome-stable \  
nodejs \  
curl \  
python \  
\--no-install-recommends \  
&& curl --silent \--show-error --retry 5 "https://bootstrap.pypa.io/get-
pip.py" | python \  
&& pip install awscli \  
&& npm --global install yarn \  
&& apt-get purge --auto-remove -y curl gnupg \  
&& rm -rf /var/lib/apt/lists/*  
  
ARG CACHEBUST=1  
RUN yarn global add lighthouse  

