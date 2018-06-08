FROM debian:jessie  
  
MAINTAINER stefan@lapers.be  
  
ADD xvfb-chromium /usr/bin/xvfb-chromium  
  
RUN set -e \  
&& echo " ------ SETTING UP COMMON PACKAGES ------" \  
&& apt-get update \  
&& apt-get -y install curl \  
\  
&& echo " ------ SETTING UP CHROMIUM ------" \  
&& apt-get -y install xvfb chromium \  
&& ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome \  
&& ln -s /usr/bin/xvfb-chromium /usr/bin/chromium-browser \  
\  
&& echo " ------ SETTING UP NODEJS ------" \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install -y nodejs \  
&& npm install -g npm@latest \  
\  
&& echo " ------ SETTING UP ANGULAR CLI ------" \  
&& npm install --unsafe-perm -g @angular/cli \  
\  
&& echo " ------ CLEAN UP ------" \  
&& rm -rf /var/lib/apt/lists/*  

