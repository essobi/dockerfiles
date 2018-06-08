FROM node:boron  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
git \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN npm install -g bower polymer-cli --unsafe-perm  
  
CMD "bash"

