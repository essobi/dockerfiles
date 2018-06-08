FROM node:8-stretch  
LABEL maintainer "Vincent Giersch <vincent+docker@flat.io>"  
  
# Install Chrome  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
ca-certificates \  
curl \  
gnupg \  
hicolor-icon-theme \  
libcanberra-gtk* \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
libpango1.0-0 \  
libpulse0 \  
libv4l-0 \  
fonts-symbola \  
\--no-install-recommends \  
&& curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
\  
&& echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main"
> /etc/apt/sources.list.d/google.list \  
&& apt-get update && apt-get install -y \  
google-chrome-stable \  
\--no-install-recommends \  
&& apt-get purge --auto-remove -y curl \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN groupadd -g 999 user && \  
useradd -m -d /home/user -r -u 999 -g user user  
USER user  

