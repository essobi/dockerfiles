FROM ubuntu:16.04  
# Update package lists and bring all package up to date.  
RUN apt-get update \  
&& apt-get dist-upgrade -y  
  
# Install dependencies for install scripts.  
RUN apt-get install -y \  
apt-transport-https \  
curl  
  
# Install Yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update \  
&& apt-get install -y yarn  
  
# Install Node.js  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y nodejs  
  
# Install Cypress dependencies (separate commands to avoid time outs)  
RUN apt-get install -y \  
libgtk2.0-0  
RUN apt-get install -y \  
libnotify-dev  
RUN apt-get install -y \  
libgconf-2-4 \  
libnss3 \  
libxss1  
RUN apt-get install -y \  
libasound2 \  
xvfb  
  
# Download Cypress binary  
RUN mkdir /opt/cypress \  
&& curl -sS https://cdn.cypress.io/desktop/2.1.0/linux64/cypress.zip >
/opt/cypress/cypress.zip  
  
# Cleanup  
RUN apt-get purge -y \  
apt-transport-https \  
curl \  
lsb-release \  
&& apt-get --purge -y autoremove \  
&& apt-get autoclean \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

