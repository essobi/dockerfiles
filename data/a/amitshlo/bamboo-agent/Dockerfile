FROM davidcaste/debian-oracle-java:jdk8  
MAINTAINER Amit Shlomovits (amut00@gmail.com)  
  
# Install Chromium and make it headless & other stuff needed  
RUN apt-get update && apt-get install -y curl xvfb chromium sudo apt-
transport-https ca-certificates gnupg2 software-properties-common  
ADD xvfb-chromium /usr/bin/xvfb-chromium  
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome && \  
ln -s /usr/bin/xvfb-chromium /usr/bin/chromium-browser  
  
# Install zip, unzip, nodejs, maven, docker & git  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - && \  
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
&& \  
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian
$(lsb_release -cs) stable" && \  
apt-get update && apt-get -y install zip unzip nodejs git docker-ce maven  
  
# Do npm stuff  
RUN npm config set prefix /usr/local  
  
# Install yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - &&
\  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && apt-get install -y yarn  
  
RUN yarn global add gulp typescript mocha forever @angular/cli  
  
# Copy files  
COPY /root /root  
  
# Add exec permission to required files.  
RUN mkdir -p /root/bamboo-agent-home/bin && \  
chmod +x /root/bamboo-update-capability.sh && \  
chmod +x /root/run-agent.sh  
  
# Run Bamboo Agent setup script  
CMD /root/run-agent.sh

