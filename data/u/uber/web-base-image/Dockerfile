FROM node:8.11.1  
RUN yarn global add yarn@1.6.0  
  
# Add our xvfb script  
RUN apt-get update && apt-get -y install libxi-dev libgl1-mesa-dev xvfb  
ADD xvfb /etc/init.d/xvfb  
RUN chmod a+x /etc/init.d/xvfb  
ENV DISPLAY :99  
# Install Chrome  
RUN apt-get update && apt-get install -y wget --no-install-recommends \  
&& wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable
main" >> /etc/apt/sources.list.d/google.list' \  
&& apt-get update \  
&& apt-get install -y google-chrome-unstable \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /src/*.deb  

