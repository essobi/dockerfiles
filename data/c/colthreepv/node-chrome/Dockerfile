ARG NODE_TAG  
FROM node:${NODE_TAG}  
  
RUN apt-get update \  
&& apt-get install -y apt-transport-https \  
&& curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
\  
&& echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main"
> /etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update && apt-get install -y google-chrome-stable --no-install-
recommends \  
&& rm /etc/apt/sources.list.d/google-chrome.list \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  

