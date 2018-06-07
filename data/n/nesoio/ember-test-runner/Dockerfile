FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
ca-certificates \  
git \  
curl \  
gnupg \  
libnss3 \  
libnss3-tools \  
libfontconfig1 \  
xvfb  
  
RUN Xvfb :10 -screen 0 1280x720x16 &  
  
RUN curl -O http://security.ubuntu.com/ubuntu/pool/universe/c/chromium-
browser/chromium-chromedriver_61.0.3163.100-0ubuntu1.1378_amd64.deb \  
&& dpkg -i --force-depends chromium-
chromedriver_61.0.3163.100-0ubuntu1.1378_amd64.deb \  
&& apt-get update \  
&& apt-get install -f -y  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && apt-get update
&& apt-get install -y nodejs  
  
RUN npm install -g ember-cli  
  
WORKDIR /usr/src/

