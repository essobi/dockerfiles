FROM node:stretch  
  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add \- \  
&& sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list' \  
&& DEBIAN_FRONTEND="noninteractive" apt-get update &&
DEBIAN_FRONTEND="noninteractive" apt-get install -y \--no-install-recommends \  
libgconf-2-4 openjdk-8-jre-headless google-chrome-stable \  
xdg-utils wget python-dev curl \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -s https://bootstrap.pypa.io/get-pip.py | python \  
&& pip install s3cmd  
  
USER node  
  
ENV CHROME_BIN /usr/bin/google-chrome-stable  

