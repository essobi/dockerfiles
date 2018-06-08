FROM node:8.4.0  
  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
apt-transport-https \  
curl \  
xz-utils \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
  
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key
add - \  
&& echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update -qqy \  
&& apt-get -qqy install google-chrome-unstable \  
&& rm /etc/apt/sources.list.d/google-chrome.list \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  

